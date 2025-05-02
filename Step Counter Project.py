#prompt user to input how many weeks they are tracking
howmanyweeks = int(input(f"How many weeks are you tracking steps for?: "))
#create variable that holds all seven days of the week in a list format
daysofweek=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#variable shows that the total number of days is weeks * 7
totaldays=howmanyweeks*7
#creates a totalsteps variable, sets it to zero
totalsteps=0.0
#create a for loop.  Will iterate between 1 and however many weeks the user entered
for weeks in range(1,howmanyweeks+1):
    #establishes which week we're on
    print(f"For Week {weeks}")
    #searches through the daysoftheweek variable, holding the days of the week in a list format
    for days in daysofweek:
        #prompts user to type in how many steps they did on that day
        daysteps=float(input(f"How many steps on {days}?: "))
        #totalsteps variable accumulates all the daily steps so we can display it later in the code
        totalsteps+=daysteps
#using fstrings, the print statements output the relevant data.  Keeps count of number of days, weeks,
#total steps, average steps.  Average steps are total steps divided by total days.
print(f"In {totaldays:} days: ")
print(f"Total Steps: {totalsteps:,.2f}")
average_steps=totalsteps/totaldays
print(f"Average Steps: {average_steps:,.2f}")
