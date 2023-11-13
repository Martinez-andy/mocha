from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# Configure application
app = Flask(__name__)


# Establish session stuff
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# The database that stores the user, expenses, and budget information
db = SQL("sqlite:///PF.db")

# These categories are used often so I created a global variable
categories = ['dining', 'groceries', 'transport', 'streaming', 'drugstores', 'travel', 'online', 'bills', 'savings']


def isdollar(input):
    # Makes sure the input isn't text, or a non-dollar qualitity
    string = str(input)
    if string.isalpha() == False:
        try:
            if ((float(input) * 100) % 1) <= 0.0001:
                return True
        except:
            return False
    return False


def isnegative(input):
    # Checks if input is negative
    if input >= 0:
        return True
    return False


def isclose(expenditure, budgeted):
    # Checks if expenditure in one category surpasses budgeted expenditure
    if expenditure == 0:
        return False
    if budgeted == 0:
        return True
    ratio = expenditure / budgeted
    if ratio > 1:
        return True
    return False


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/dash")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        # Display registration form
        return render_template("register.html")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    username = request.form.get("username")
    # Checks passwords and username
    if not password or not confirmation:
        return apology("Please fill out both password fields")
    if not username:
        return apology("Please enter a username")
    if password != confirmation:
        return apology("Passwords do not match")
    for element in db.execute("SELECT username FROM users"):
        if username in element["username"]:
            return apology("Username already in use")
    password = generate_password_hash(password)
    # Adds user into the system
    db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, password)
    # Logs the user in
    session["user_id"] = (db.execute("SELECT id FROM users WHERE username = ?", username))[0]["id"]
    db.execute("INSERT INTO expenses (user_id) VALUES(?)", session["user_id"])
    db.execute("INSERT INTO budget (user_id) VALUES(?)", session["user_id"])
    return redirect("/dash")


@app.route("/dash")
@login_required
def dash():
    # These counters count how many 0s there are in temp1 and temp2
    counter1 = 0
    counter2 = 0
    temp1 = db.execute(
        "SELECT dining, groceries, transport, streaming, drugstores, travel, online, bills, savings FROM expenses WHERE user_id = ?", session["user_id"])[0]
    temp2 = db.execute(
        "SELECT dining, groceries, transport, streaming, drugstores, travel, online, bills, savings FROM budget WHERE user_id = ?", session["user_id"])[0]
    # If there are 9 zeros then we know the data table hasn't been edited so we should display the placeholder pie charts
    for element in temp1:
        if temp1[element] == 0:
            counter1 += 1
        if temp2[element] == 0:
            counter2 += 1
    # Initializes the data so that the piechart can read it
    data1 = {"Category: ": "Expenditure :"}
    data2 = {"Category: ": "Planned Expenditure"}
    # appends the data onto the previous dictionary
    data1.update(temp1)
    data2.update(temp2)
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])
    expenses = db.execute("SELECT * FROM expenses WHERE user_id = ?", session["user_id"])[0]
    planned = db.execute("SELECT * FROM budget WHERE user_id = ?", session["user_id"])[0]
    # Stores all the categories that have exceeded their budget allocation
    close = {}
    for element in categories:
        if isclose(expenses[element], planned[element]):
            try:
                close[element] = expenses[element] / planned[element]
            except:
                close[element] = str(expenses[element])
    return render_template("dash.html", data1=data1, data2=data2, transactions=transactions, close=close, counter1=counter1, counter2=counter2)


@app.route("/budget", methods=["GET", "POST"])
@login_required
def budget():
    if request.method == "GET":
        return render_template("budget.html", categories=categories)
    # Load input into variables
    category = str(request.form.get("category"))
    expense = request.form.get("expense")
    # Check for proper input and return an error if improper
    if not expense or isdollar(expense) == False:
        return apology("Input a dollar amount")
    # Check for proper input and return error if improper
    if category not in categories or category == None:
        return apology("Category error")
    expense = float(expense)
    tmp = db.execute("SELECT * FROM budget WHERE user_id = ?", session["user_id"])
    prev = tmp[0][category]
    # Check if negative input causing column to be negative
    if isnegative(expense + prev) == False:
        return apology("Improper dollar input")
    # Update data and bring back to dashboard
    db.execute("UPDATE budget SET ? = ? + ? WHERE user_id = ?", category, prev, expense, session["user_id"])
    return redirect("/dash")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "GET":
        return render_template("add.html", categories=categories)
    # Load input into variables
    category = str(request.form.get("category"))
    expense = request.form.get("expense")
    # Check for errors in input
    if not expense or isdollar(expense) == False:
        return apology("Input a dollar amount")
    if category not in categories or category == None:
        return apology("Category error")
    expense = float(expense)
    tmp = db.execute("SELECT * FROM expenses WHERE user_id = ?", session["user_id"])
    prev = tmp[0][category]
    # Check is negative input causing column to be negative
    if isnegative(expense + prev) == False:
        return apology("Improper dollar input")
    # Update columns
    db.execute("UPDATE expenses SET ? = ? + ? WHERE user_id = ?", category, prev, expense, session["user_id"])
    db.execute("INSERT INTO transactions (category, amount, user_id) VALUES(?, ?, ?)", category, expense, session["user_id"])
    return redirect("/dash")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")