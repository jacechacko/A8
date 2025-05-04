1. Birthday Dictionary program:

The birthday dictionary program tests our knowledge of dictionaries and how to extract values from them.  It also checks our understanding of value passing functions.  In this program, the user inputs any number between 1-6.  Based on the inputs, the user can either show all, add, modify,delete or quit the program.  I changed the program to account for potential errors.  The main function uses if/elif to determine which number was inputted.  At this point, the assoicated function is called.  




2. Calculating_Taxes_GUI:

This program tests our understanding of the tkinter GUI module.  We create a series of widgts for this program.  We have labels for the text values of property value, assessment value, propety tax.  The two buttons are quit (using the .destroy method) and calculate, which when clicked, executes the logic of the calculation function.  The stringvar widget dynamically changes based on way the assessment value and property tax change.  The input in the GUI is the propety value, which the user can input to dynamically change the two StringVar widgets.

3. Cookout_Calculator:

This program was created during the first few weeks of class to test my understanding of Python.  This word problem is provided by our textbook at the end of chapter 3.  Basically, the user is asked how many people are attending the cookout, and how many hot dogs they are going to eat.  It then determines how many hot dogs, and buns are required.  Buns comes in packs of a certain amount, while hotdogs come in packs of a different amount.  The program must determine how many packs of each to buy, in addition to determining the number of leftovers.  In order to do this, I learned to use the math.ceiling function to always find a number rounded up.  The reason why this is crucial for the progrma to run properly is because we cannot have less packs than needed.  For example, if we need 6.2 packs of buns, we cannot round down and buy six.  We must must seven to ensure all guests have a hotdog bun.  While rounding is easy to do in Python, it is a bit more difficult to always round up.  This program was helpful in learning this.

4. Dice_Roll_Game:

  The dice roll games was one of our Individual Assignments.  Basically, two players roll individual dices and the player with a higher number wins.  The program keeps track of how many games you played, how many wins/losses/ties ocurred, and who the overall winner was.  In addition, exception handling was used to ensure that proper inputs were given so as to not break the program.  Also, f-strings and tabs were used to provide a clean output.

5. Functional Calculator:

The calculator application was one of our Individual Assignments.  Basically, it integrated our knowledge of tkinter, value passing functions, conditional logic, etc.  The user can input a first number, an operator, and then a second number, press equals, and receive the appropriate output.  This program requires the undestanding of StringVar, labels, buttons, functions, built in Python methods .get and for calculation as well.

6. Rainfall Estimator:

    The Rainfall estimator was one of our Individual Assingments.  The user is asked for how many years they are tracking for, and the rainfall for each month.  They are then shown the amount of rain that fell in total for all the years.  I added a series of additional logic to improve the program.  There is exception handling used throughout the progrma to ensure proper numbers are inputted.  There are also while loops to ensure negative numbers cannot be inputted for rainfall, years, or months.  This program helped our understanding of for loops, accumulator variables, functions, global variables, and f strings.

7. Step Counter Project:

    The step counter project was used as an in class assignment to prepare us for the rainfall estimator.  The user is prompted to input the number of weeks they are tracking for, and the steps walked each day.  They are then told the total and average number of steps walked for the total duration.  This program reinforced our understanding of for loops, accumulator variables, input functions, f strings, and more.  

8. Talent SEek 2.3 A8:  This was our group project.  I added it in case it was needed.  Explanations for the group project can be found in our Project Documentation.

9. ATM_App (NO GUI): This program was made during the very early stages of the semester and involves only basic if/elif/else statemnts, as well as accumulator variables.  The main logic is inside of a while loop, which keeps the program running until the sentitnel is called.  (Which for this program is "y").  The user is prompted to enter a number which corresponds to an action (check, deposit, withdraw, exit).  The accumulator is able to keep track of the total balance, which changes based on deposits/withdrawls.  Because this was made during the first few weeks of the semester, I did not use any exception handling as we hadn't learned it yet.

10. ATM App (With GUI):This program was made after learning tkinter in class.  I took the previous ATM app I created and added GUI code to make it more user friendly. The code puts each of the three main actions into functions, and uses balance as a global variable.  The application allows the user to type a number into the entry box, and either deposit or withdraw an amount of money.  The StringVar is updated based on the user action.  The main widgets used are buttons, labels, entries, etc. Geometry sets the dimensons, and title sets the title.  Again, the main logic is similar to the previous program, where the balance variable is updated by the deposit/withdrawl amount with the use of an accumulator.
