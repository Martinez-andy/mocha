    How did I make the web application? Well I think we should start with what I think is the prettiest page on the whole website—the homepage.
I created my own header by using an unordered list and I used css to format it to look like a nav bar at the top of the screen. The logo
disappearing behind the golden portion of the screen takes advantage of layers in css/html. The logo falls behind the golden div layer,
which creates this cool effect seeing as the logo's color is the same color as the golden div. Next, there are two smaller divs
within the golden one. To give them that pill shape I used css' border-radius and kept experimenting until I liked the appearance of the divs.
Now, the sign in and sign up pages are reminiscent of the sign in and sign up pages from finance. There are a few differences by the main
ones are in the color. I made entire website follow the same color palatte and I think it gave the website a nice cohesive feel.

    Once logged in, you will see two sample pie charts. I opted to have default charts because an empty screen would be jarring to look at.
For the piegraphs, I used and editted the ones that google shows on google charts. The main difference with this graph is that it displays
data dynamically. Having the google chart display the data as you input it was a challenge because the data was stored in an sql database.
That is not a bad thing, but the format that the db.execute returns was difficult to adapt into the format that the piechart by google uses.
In addition, the dynamic charts merged ALL possible web elements for this project. What I mean by that is that I had to use python, sql, jinja,
javascript, html, AND css just to have the piegraph display the users' data. Needless to say, doing so was a syntactic nightmare and required a
lot of hours and googling how to merge all these languages and whether I could even use jinja in a script. Before I get too deep into the programming
process I should talk about the databases.

DATA BASES:

I had one sql database called PF.db and this data base had 4 tables in total. All these tables were linked through the user's id number.
The first table I made was the users table which holds the user's credentials. The next one I made was the expenses table. For the expenses
table I had to include columns for each spend category and I defaulted all the values to zero because otherwise it would cause the piechart
to display an odd 100% piechart. That is another reason I opted to have sample piecharts for when the user has not input any data. Again,
this table tracks the total expenses for each user. This is going to become a reoccuring theme but the budget data base is nearly identical
to the expenses table for all the same reasons. Also, the user's expenses and their budget are inextricably linked so it makes sense for the two
to be so similar. The final table I included was teh transacitons table. This was actually a last minute addition. I was looking through simlar budgeting
apps and banking apps to try and see what other features I could add and realized that they all showed a list of your expenses. Therefore, I had
to make a new table that would hold all the neccessary data to log transactions.

Now, Why did I opt to display the buget and expenses on a piechart? The reason I chose the piechart was because budgets and expenses are heavily
reliant on percentages. Hence why most budgeting rules follow percentage rules (like save 15% of your income) and the piechart is a nice way
to visualize how one is spending their money. The table for the trasactions was not too dissimilar from the history tab in finance so I
used the table from there with modifications so that they fit the color palette. Now, as mentioned before, the thing I spent the most
time on were the piecharts. The issue with the altering the pie charts in real time is the difference in data formatting. When using db.execute
it returns a list of 1 element, and that one element is a dictionary. Which is fine for working with python on its own, but the google chart instead
opted to take a list of lists as its input. So I had to convert a list with a dicitonary as its only element into a list of lists. Which was not fun,
especially when I had to edit the javascript of the piecharts so that I could have two of them on the screen.

The goal of the entire application was to make it simple, and user friendly. That, however, came at the cost of my sanity with this next feature: adding
expenses and editing budgets. The html itself was borderline trivial seeing as it is almost identical to my sign in and sign up page. The html was not
the issue, the error handling was though. Since I wanted to allow for the input of some deicmal values as well as some negative values (so long as certain
conditionas were met), it made checking for errors rather difficult. The main issue is that python (at least not that I could find) does not have a
.isfloat or .isdecimal method for strings. .isdigit() and any other comparable methods do not work in this case because the decimal counts as a
"special character" and is not alphanumeric. This error checking gets even worse when you have to disallow strings as inputs because if I use something
like .isalpha() or .isalnum then if the user input a decimal value (like 0.01 for example), then the program would spit out the apology function because
the decimal point is not alphanumeric! Okay, so maybe the way to go is to first handle the case where the input is a decimal and then take care of the
other possible errors? The only problem is (at least with the method I opted to convert a dollar decimal into an int so that I can use .isdigit()) that
using my method of multiplying by 100 and then using % 1 would result in an internal server error because you cannot mulitply a string by a num. I opted
to use (100 * expense) % 1 because this should return 0 for any value to two decimal places. So, to mitigate the string error I used a try: and except:
functions/operators in python. You would think that that's where the errors stop, right? Wrong! For some reason (I assume this is related to floating
point imprecision) whenever I input 65.01 the program would incorrectly label this as an invalid input. Not 65.02, or 65.00, but precisely 65.01 as well
as some multiples of 65.01 such as 130.02 among others. I spent quite some time trying to figure out why my function was breaking at these particular
values and decided to print out the value of the remainer according to the computer. Once I did, I saw that the value which was supposed to be zero
was not zero. Instead, the value was in scientific notation and might as well have been zero. After a few tries of trying to work out the issue I
opted to simply change one of the if statements, so (100 * expense) % 1 no longer has to equal exactly zero, but instead it should be
reallllllllly close to 0.

    Once I had accounted for all the errors, the webapplication was complete! One thing I would like to note is that I originally had 4 different
hmtl files, one for each possibility of the user not having put in data for the budget or expense piechart. However, I knew that the implementation
was not well designed, nor was it scalable! So I did some research on javascript and I managed to make the piecharts change automatically (no need for
the additional 3 html files, just the normal dashboard.html)! I did this because I looked at the google charts and realized that in the html the piechart
was just the id, the real chart making was done in the javascript. So, I used javascript to change the id of the div (essentially change the piechart
from sample to the one with data) as soon as the sql tables were editted. I am pretty proud of this because it was a pretty simple and elegant solution.