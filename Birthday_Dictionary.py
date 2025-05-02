#create a function where user can input their menu choice via the input function.
def get_menu_choice():
    choice =int(input("""Here are your options:   

    1. Look up a particular person's birthday
    2. Add a new birthday
    3. Change a birthday
    4. Delete a birthday
    5. Quit the program
    6. Show all names/birthdays in the list

Enter a number between 1 and 6 to perform associated command: """))
    #choice is returned so that when we later call the function, this logic is done.
    return choice
#create a function for looking up a birthday
def look_up(birthday_dictionary):
    #prompts user to input the name of the friend.
    friend_name =input("Enter your friend's name to look them up: ")
    #conditional logic-if they name exists in the dictionary, show when they were born (using f-strings)
    if friend_name in birthday_dictionary:
        print("                   ")
        print(f"Your friend {friend_name} was born on: {birthday_dictionary[friend_name]}")
        print("                   ")
        print("Name looked up!")
        print("                   ")
        print("--------------------")
        #if name isn't found, tell user the name wasn't found
    else:
        print("                   ")
        print("Name not found!")
        print("                   ")
        print("--------------------")
        #create function to add an entry to the master list
def add(birthday_dictionary):
    #prompts user to add name of a friend to add to them lsit
    friend_name =input("Enter your friend's name to add them: ")
    #prompts user to add birthday of that friend
    birthday =input("Enter the birthday of the friend")
    #conditional statement-if friend's name isn't found, it means it can be added.  This is to prevent duplicates.
    if friend_name not in birthday_dictionary:

        birthday_dictionary[friend_name ] =birthday
        print("                   ")
        print("Name added!")
        print("                   ")
        print("--------------------")
        #conditional logic-else statement catches duplicates.  Duplicates will not be appended to master list.
    else:
        print("                   ")
        print("Enter a unique name to prevent accidental duplicates")
        print("                   ")
        print("--------------------")
#create a function to modify entries in the dictionary.
def change(birthday_dictionary):
    #prompts user to input the friend's name for change
    friend_name =input("Enter the name of the person whose bday you're changing: ")
    #conditional logic-if friend's name exists in dictionary, it asks user what the birthday is.
    if friend_name in birthday_dictionary:
        new_birthday =input("Enter the new birthday: ")
        birthday_dictionary[friend_name ] =new_birthday
        print(f"Name successfully changed!")
        print("                   ")
        print("--------------------")
        #conditional statement-if name isn't found in dictionary, it can't be changed.  User is informed that the friend's name cannot be found.
    else:
        print("                   ")
        print(f"Unable to find {friend_name}. ")
        print("                   ")
        print("--------------------")
        #this function allows user to delete a record in the dictionary
def delete(birthday_dictionary):
    #prompts user for friend's name for deletion
    friend_name =input("Enter the name of the person you want to delete: ")
    #sees if the inputted name is in dictionary.  If so, the del keyword deletes the entry from dictionary.  User is informed of
    #this in the print statement (with f-strings).
    while True:
        if friend_name in birthday_dictionary:
            del birthday_dictionary[friend_name]
            print(f"You just deleted {friend_name} and their associated birthday.")
            print("                   ")
            print("Name/birthday successfully deleted!")
            print("                   ")
            print("--------------------")
    #conditional statement - if name isn't found, it cannot be deleted, and user is informed name couldn't be found.
        else:
            print("                   ")
            print("Name not found.")
            print("--------------------")
        break

#this function lets the user see all elements of the dictionary
def show_all(birthday_dictionary):
    #if the dictionary holds no value, user is informed the dictionary is empty
    if  birthday_dictionary == {}:
        print("The birthday list is empty.")
        print("                   ")
        print("--------------------")
#conditional logic - if there is infact anytihng in the dicitonary, it will iterate over a for loop, where all the 
    #key and value pairs (meaning all the records) of the dictionary are displayed for the user to see.
    else:
        for key, value in birthday_dictionary.items():

            print(f"Name: {key} -- Birthday: {value}")
            print("                   ")


#main function initiates the core logic of the function
def main():
#sets an empty dictionary
    birthday_dictionary ={}
    while True:
        #the number pressed dictates what action the program takes
        choice =get_menu_choice()
#conditional logic-with these if/elif statements, the number inptutted will determine which function is called
        if choice == 1:
            look_up(birthday_dictionary)
        elif choice == 2:
            add(birthday_dictionary)
        elif choice == 3:
            change(birthday_dictionary)
        elif choice == 4:
            delete(birthday_dictionary)
        elif choice == 5:
            print("Bye!")
            quit()
        elif choice==6:
            show_all(birthday_dictionary)


#activates the main function
main()
