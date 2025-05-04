balance =1000
deposit=0
withdraw=0
is_running = "y"
while is_running == "y":

    userinputnumber = int(input("""Please enter 1 to check balance, 2 to deposit funds, 3 to withdraw  money, and 4 to Exit:\n"""))
    if userinputnumber ==1:
        print(f"Your balance is ${balance:,.2f}")
    elif userinputnumber ==2:
        deposit=float(input(f"How much would you like to deposit?: "))
        balance += deposit
        print(f"You deposit ${deposit:,.2f}.  Your balance is now: ${balance:,.2f}")

    elif userinputnumber == 3:
        withdraw = float(input(f"How much would you like to withdraw?: "))
        balance -= withdraw
        print(f"You withdraw ${withdraw:,.2f} and now have a balance of ${balance:,.2f}")
    elif userinputnumber == 4:
        print("Exiting application.  Have a good day")
        is_running = 'n'
    else:
        print("Invalid number.  Please Enter a number between 1-4")
