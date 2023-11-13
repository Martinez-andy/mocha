    Hello there reader, my name is Andy Martinez and this is my final project for CS50—a budgeting and expense tracking application!
I will walk you step by step as to how to use the application—Mocha. Let's start with the hompage, on the top left you will see
our text logo, this will serve as a homepage regardless of which page you are on. Whether you are logged in or not, clicking on
logo in the top right corner will bring you to the home (for now) or dashboard (we will cover this later). On the top right portion
of the screen you will see sign in and sign up buttons which, as their names suggest, you can use to either create an account or log
into your account if you are a returning user. If you scroll down you will see the cool effect with our main logo in which is seems
to disappear as you scroll down. Below that, a short introduction to Mocha: the all in one financial tool!

    Since you are a new user, click on the top right to sign up, enter a username, password, and then confirm the password. If you decide
to return to the webstie (which we hope you do) click on the log in button and enter your credentails to access your data. Now that you're in
you should be brough to the dashboard. The dashboard is the new "home" and the Mocha Logo on the top left will now return you back to this
dashboard page. On the dash board, you will see two sample pie charts. Those piecharts are placeholders for now, but your expenses and budget
will go right where does piecharts currrenlty are. Speaking of budgets and expenses, you should begin planning your budget right now! On the
top right of the screen, where the sign in and sign up buttons used to be, you will see a few new buttons! We will get to them in just a bit
but for now, let's focus on the "Edit Budget" button. Click on it and you will be redirected to another page! On this new page, you should see
a drop down menu and a little textbox. To add a budget category/edit one you simply select a category from the drop down menu, and enter a valid
dollar quantity. The program will automatically reject any improper text inputs. Now, you should click the edit budget button to submit the edit!

    Now that you have added a category to your budget you will be redirected to the dashboard. Not only that, but look! The piechart for your budget
reflects the edit you've made. However, you might have made a mistake when creating a budget, or maybe you realize that you've allocated too much
money to a particular category. Fret not, for editting a budget is just as easy as inputting a new category. To edit a budget, you should still click
on the edit budget button. The cool thing about this form is that it takes in positive AND negative dollar values (including the 2 decimal places).
So, if you want to decrease the amount of money you have allocated to a category, just input a negative number. Caution: the form does accept negative
dollar values but it automatically rejects any alterations that would leave you with a negative balance within a category. If you want to allocate more
money to a category, you again click the edit budget button and input how much money you would like to add to a category.

    Since you've already started your first budget, why don't you go ahead and record an expense. On the top right corner, click on the Add Expense button.
You should be directed to a page that looks similar to the edit budget page. Here, you again add a category for an expense and input a valid dollar value
and the website will then redirect you to the dashboard and the expenses piechart should reflect your edits. Against, what if you've made an error in your
expense tracking or what if you got a refund for an item? Well, much like the edit budget form, the add expense form also accepts negative inputs so long as
those negative inputs do not cause you to have a negative balance in a specific category. So, if you input an expense of 100 dollars when you meant to input
10, then all you have to do is click the add expense button and input -90. The changes will be reflected on the piechart on the dashboard.

    If you were curious to see what sort of bugs you could find, then you may have tried inputting an expense that exceeded your budget's allocation
Potentailly, you could have even tried inputting an expense that you haven't budgeted for at all. If either one of these apply to you, then you should
have been met by an alert before you could proceed. Mocha sends you an alert any time you input an expense that exceeds your budgeted amount (especially
when the budget category has not been set yet). The program will continue to alert you of your overexpenditure until the issue is addressed. You could
address the underbudgetting by either increasing the budget expense category or by decreasing the expenditure (by using edit budget or add expense
respectively). That way the application pushes you towards making the right decision and sticking to the budget which is essential to financial success.

    If you are following along with this README.md file, then you may have also noticed that something (other than the pie charts) has changed
in the dashboard. That's right, Mocha even tracks your transactions! Under both pie charts, after inputting an expense, you will see a table that contains
your transaction log. Within the transaction logs you can see how much you spent, the category you spent it in, the time the expense occured, and counts
how many transactions you have had.

Youtube link:
https://youtu.be/1a5VJU1rTxk
