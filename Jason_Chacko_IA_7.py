#Individual Assignment 7: Dice Roll Game
# *Note: My output will look different because of spacing. I wanted to make it easier to identify individual
#games and the final score.

#first import the random library, which will allow us to use the randint method later on
import random

#Create a function called roll_dice.
def roll_dice():

#Create dice_chance variable, with randit method.  This will assign the variable a random number between 1-6.
#I didn't assign a max and min variable because all dices have 6 sides and 6 values, that won't change.

    dice_chance=random.randint(1,6)
#return the value of the random number to the dice_chance variable.  When we call this function later in the
#main function, it will simulate the rolling of a six sided die.
    return dice_chance

#create a function called play_round.  This function dictates the behavior of the dice game
def play_round(player1_move, player2_move):

#If Player 1's dice roll is a larger number than Player 2's dice roll, it successfully passes the if statement and
#will print out the logic within the if statement, with f strings used to space everything properly.
    if player1_move>player2_move:

        print(f"Player 1 rolls a die and gets a {player1_move}.\n"
        f"Player 2 rolls the die and gets a {player2_move}.\n"
        f"Winner of the round is: Player 1.\n"
        f"----")

#If Player 2's dice roll is a larger number than Player 1's dice roll, it passes the elif statement and
#will print out the logic within the elif statement, with f strings used to space everything properly.
    elif player2_move>player1_move:

        print(f"Player 1 rolls a die and gets a {player1_move}.\n"
        f"Player 2 rolls a die and gets a {player2_move}.\n"
        f"Winner of the round is: Player 2.\n"
        f"----")

#If neither Player's number is larger than the other, they must be equal.  Therefore, it will be caught in the
#else statement, which will print out the statement that both players got the same number.  Again, f strings are
#used here to properly allow for formatting and the variable name within the statement.  It shouldn't matter
#if the variable in the f string is player1_move or player2_move since they should be the same in the event of
#a tie.
    else:

        print(f"Both players rolled the dice and got a {player1_move}.  The round ends in a tie.")

#Create a main function, which houses the main logic to carry out the dice roll program
def main():
#first initialize the score variables for player 1 score, player 2 score, and a tied score
#This is similar to how we did the rock paper scissors problem for class.  These variables will keep track
#of how many rounds each player is winning, or if there was a tie.  At the end, the player with most pts
#will win game.
    player1_score = 0
    player2_score = 0
    tied_score = 0

#The while loop will be used to ensure that the userinput of number of rounds is both a
#positive integer.  The exception handling will use a try/except block to ensure
#a proper number is inputted (ValueError check).  If a negative number is entered, it rejects it. If
#a decimal or string or symbol is inputted, it is rejected because of ValueError.
    while True:
#try/except validation
        try:
            rounds = int(input("How many rounds do you want to play? "))
#checks to ensure the user input is positive.  If user enters zero for rounds input, then the game will
#process zero dice rolls, and since neither user has pts, it will end in a tie.
            while rounds<0:
                print(f"Number of rounds cannot be less than zero.  Enter a positive number.")
                rounds = int(input("How many rounds do you want to play? "))
#loop breaks once the input is positive
            break
#if a character like "$", or a number like 1.5 is inputted, it will raise ValueError
#and again ask user to input a valid number.
        except ValueError:
            print(f"Invalid Response. Please enter a valid integer for number of rounds")

#create a for loop to iterate all of the games that the user requested
    for round in range(rounds):
#create a variable called player1_throw, which will call the roll_dice function. This will
#assign the variable to a random number between 1-6.
        player1_throw = roll_dice()
#create a variable called player2_throw, which will call the roll_dice function. This will
#assign the variable to a random number between 1-6.
        player2_throw = roll_dice()
#This print statement will be used as a header for each game, so the user knows which results are for which round.
#it is round+1 because the default of the iteration starts at zero.  This is the same kind of logic we used
#for the temperature tracker for motnhs assignment.

        print(f"\nGame {round + 1}:")
#calls the play_round function, and passes the player1_throw and player_2 variables as parameters of the function
        play_round(player1_throw, player2_throw)
#conditional statement-if the random number assigned to player 1 is equal to the random number assigned to
#player 2, it adds to the counter for the tied score.
        if player1_throw == player2_throw:
            tied_score += 1
#conditional statement-elif the random number assigned to player 1 is larger than the random number assigned to
#player 2, it adds to the counter for the player1 score.
        elif player1_throw > player2_throw:
            player1_score += 1
#conditional statement-else catches all else, and when the random number assigned to player 2 is
#larger than the random number assigned to  player 1, it creates a counter for the player2 score.
        else:
            player2_score += 1

#This final print statement displays the resulting scores, based on the values of the throws
#Print statement uses f strings, \n for new lines, curly braces for variables.  I adjusted the print statement
#output for readability and to tell the different games apart.

    print(
        f"\nFinal Score: \n"
        f"Player 1 wins: {player1_score} round(s).\n"
        f"Player 2 wins: {player2_score} round(s).\n" 
        f"{tied_score} round(s) ended in a tie.")

#Conditional statement - if player 1's score is larger than player 2's score, announce player 1 as winner.
    if player1_score > player2_score:
        print(f"\nOverall Winner: Player 1!")

#Conditional statement - elif player 2's score is larger than player 1's score, announce player 2 as winner.
    elif player2_score > player1_score:
        print(f"\nOverall Winner: Player 2!")

#Conditional statement - else statement catches all else.  If player 1's score is equal player 2's score, announce
#that the game has ended in a tie.
    else:
        print(f"\nThe game ends in a tie!")

#Call the main function to execute the logic within, and this will start the program.  This is the
#notation we used in class for calling the main function, rather than the main() call we used earlier in semester.
if __name__ == "__main__":
    main()





