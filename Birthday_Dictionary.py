
def get_menu_choice():
    choice =int(input("""Here are your options:   

    1. Look up a particular person's birthday
    2. Add a new birthday
    3. Change a birthday
    4. Delete a birthday
    5. Quit the program
    6. Show all names/birthdays in the list

Enter a number between 1 and 6 to perform associated command: """))
    return choice

def look_up(birthday_dictionary):
    friend_name =input("Enter your friend's name to look them up: ")
    if friend_name in birthday_dictionary:
        print("                   ")
        print(f"Your friend {friend_name} was born on: {birthday_dictionary[friend_name]}")
        print("                   ")
        print("Name looked up!")
        print("                   ")
        print("--------------------")
    else:
        print("                   ")
        print("Name not found!")
        print("                   ")
        print("--------------------")
def add(birthday_dictionary):
    friend_name =input("Enter your friend's name to add them: ")
    birthday =input("Enter the birthday of the friend")
    if friend_name not in birthday_dictionary:

        birthday_dictionary[friend_name ] =birthday
        print("                   ")
        print("Name added!")
        print("                   ")
        print("--------------------")
    else:
        print("                   ")
        print("Enter a unique name to prevent accidental duplicates")
        print("                   ")
        print("--------------------")

def change(birthday_dictionary):
    friend_name =input("Enter the name of the person whose bday you're changing: ")
    if friend_name in birthday_dictionary:
        new_birthday =input("Enter the new birthday: ")
        birthday_dictionary[friend_name ] =new_birthday
        print(f"Name successfully changed!")
        print("                   ")
        print("--------------------")
    else:
        print("                   ")
        print(f"Unable to find {friend_name}. ")
        print("                   ")
        print("--------------------")
def delete(birthday_dictionary):
    friend_name =input("Enter the name of the person you want to delete: ")
    while True:
        if friend_name in birthday_dictionary:
            del birthday_dictionary[friend_name]
            print(f"You just deleted {friend_name} and their associated birthday.")
            print("                   ")
            print("Name/birthday successfully deleted!")
            print("                   ")
            print("--------------------")

        else:
            print("                   ")
            print("Name not found.")
            print("--------------------")
        break


def show_all(birthday_dictionary):
    if  birthday_dictionary == {}:
        print("The birthday list is empty.")
        print("                   ")
        print("--------------------")

    else:
        for key, value in birthday_dictionary.items():

            print(f"Name: {key} -- Birthday: {value}")
            print("                   ")



def main():

    birthday_dictionary ={}
    while True:
        choice =get_menu_choice()

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



main()
