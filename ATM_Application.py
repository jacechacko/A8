#Create Global constants for balance, deposit, withdraw
balance =1000
deposit=0
withdraw=0

#sets sentinel, so the while loop has a chance to stop
is_running = "y"
#create a while loop, program runs for as long as the is_running variable is set to "y"
while is_running == "y":

    #user inputs a number, which corresponds to check balance, deposit, withdraw, exit
    userinputnumber = int(input("""Please enter 1 to check balance, 2 to deposit funds, 3 to withdraw  money, and 4 to Exit:\n"""))
    #if user inputs 1, the balance variable is displayed
    if userinputnumber ==1:
        print(f"Your balance is ${balance:,.2f}")
        #elif user inputs 2, the deposit amount is asked to user, and the balance variable adds the deposit amount
    elif userinputnumber ==2:
        deposit=float(input(f"How much would you like to deposit?: "))
        balance += deposit
        #user is shown updated balance
        print(f"You deposit ${deposit:,.2f}.  Your balance is now: ${balance:,.2f}")
        
#elif user inputs 3, the user is asked the withdraw amount, and that amount is subtracted from the balance
    elif userinputnumber == 3:
        withdraw = float(input(f"How much would you like to withdraw?: "))
        balance -= withdraw
        #user is shown new balance
        print(f"You withdraw ${withdraw:,.2f} and now have a balance of ${balance:,.2f}")
        #elif user wants to exit app, user inputs 4. The sentinel changes to "n" and so the while loop break, program stops.
    elif userinputnumber == 4:
        print("Exiting application.  Have a good day")
        is_running = 'n'
        #if user inputs a number not between 1-4, the user is prompted to enter a valid number.
    else:
        print("Invalid number.  Please Enter a number between 1-4")
