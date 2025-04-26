#IA 5 - Rainfall Tracker

#Establish global variables that will be used within the functions
total_rainfall=0
years=0
total_months=0
#create main function, which will call all the functions we create to gather data, calculate, and diplay.
def main():
    input_yearsandmonths()
    calculate_rainfall_amount()
    rainfall_results()
#This first calls the global variables we established at the beginning of the code.
#This function, input_yearsandmonths, will be used to prompt user for the number of years they want data for, and
#also establishes the month variable with an array of values that are the months of the year, in string form.

def input_yearsandmonths():
    global years
    global months
    global total_months
#Error catching - first for negative values for years, then to make sure valid number is inputted for years.
    while True:
        try:
            years = int(input(f"Enter the total number of years: "))
#This is less than or equal to because if zero is passed, it will create a divide by zero error if user
#inputs zero.  Year value can never be zero.  If years could be zero, a zerodivision error catch would be
#used later in the code.
            while years <= 0:
                print(f"Please enter a positive number for years.")
                years = int(input(f"Enter the total number of years: "))
            break
#if user inputs anything other than a number, the error is handled
        except ValueError:
            print(f"Please enter a valid year")
#variable holding an array of string values.  Will be cycled through in the second for loop, in the calculate function.
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
#total_months variable keeps track of the total months of data we are look at.  This is number of years * 12 months in a year
    total_months = years * 12

#This next function, calculate_rainfall_amount, creates a nested for loop structure which keeps track of how many
#years we are looking at, cycling through those years, and cycling through all of the months for each of those years.

def calculate_rainfall_amount():
#call global variables we set earlier
    global months
    global years
    global total_rainfall
#outer for loop establishes that for however many years the user inputted earlier, it will loop through that many years
    for year in range(1, years + 1):
        print(f"For Year {year}: \n") #will print the name of that year
#inner for loop prompts user to input amount of rainfall for each of the 12 months, for each year user specified
        for month in months:
#Error catching - first catches negative values for rainfall, then non number values.  Will screen these values out.
            while True:
                try:
                    rainfall = float(input(f"Enter the rainfall amount for {month}: "))
#This while loop is less than zero instead of <= because rainfall could be zero, while years variable earlier cannot be zero.
                    while rainfall<0:
                        print(f"Rainfall must be a positive number")
                        rainfall = float(input(f"Enter the rainfall amount for {month}: "))
                    break
#Error catching - any non-numbers will be screened out
                except ValueError:
                    print("Enter a valid number for rain amount")
#the total_rainfall variable aggregates all of the rainfall amounts the user inputted.  For example, if user
#inputted 3 years, that is 36 months.  It will cycle through all 12 months 3 times, asking for rainfall amounts.
#at the end, the program will add up all 36 values to get rainfall total amount.
            total_rainfall += rainfall

#This function, rainfall_results, will be used to display all of the data about rainfall including
#totals number of months, total rainfall, and average monthly rainfall.

def rainfall_results():
#calls global variables defined earlier
    global total_rainfall
    global total_months
#This print statement will call the total_months variable, which is the number of years user inputted * 12
    print(f"For {total_months} months:")
#This print statement will call the total_rainfall variable, which was the accumulator we used earlier to collect
#rainfall totals within our for loops.
    print(f"The total rainfall: {total_rainfall:,.2f} inches.")
#create new variable, average_monthly_rainfall, which divides the total rainfall by the total number of months the user wants information for.
#No zero division error handling needed for this variable.  This is because we screened out inputs of zero for
#the input year, since year is always >0.  Even if only the first 9 months are tracked, the year would be 1, and
#the first 9 months would have values, last 3 months would simply be inputs of zero.
    average_monthly_rainfall = total_rainfall / total_months
#This print statement displays the average monthly rainfall with the variable average_monthly_rainfall
    print(f"The average monthly rainfall: {average_monthly_rainfall:,.2f} inches.")

#This calls the main function, which will execute all of the other functions specified within it
main()
