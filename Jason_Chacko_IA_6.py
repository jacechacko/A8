#Individual Assignment #6: Making a calculator, with GUI

#First import the GUI library, tkinter.  We use an alias of "tk" for shorthand
import tkinter as tk
from tkinter import StringVar

#Creating the main window
main_window=tk.Tk()
#Geomoetry method sets the size of the window
main_window.geometry("312x324")
#Title method sets the title of the window
main_window.title("My Calculator")

#Set global variables to be used throughout the program, empty
expression = ""
input_text = StringVar()

#Creating functions to handle behavior

#Function 1: btn_click.  This function establishes what happens when a button is clicked

def btn_click(item):
    global expression #call global variable
    expression=expression + str(item)
    input_text.set(expression)

#Function 2: btn_clear.  This function will clear the field as needed.
def btn_clear():
    global expression
    expression=""
    input_text.set("")

#Function 3: btn_equal.  This function evaluates whatever math you do, will direct behavior of the equals button later on.
def btn_equal():
    global expression
#Create a try/except error validation to ensure invalid data is filtered out
    try:
        result=str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression=""

#This next part of the code will establish the actual GUI

#Creation of the frames

#This first frame is the top frame for input field
input_frame=tk.Frame(main_window, width=312, height=50, bd=0,highlightbackground="black", highlightcolor="black", highlightthickness=1)
#pack the input frame with pack()
input_frame.pack(side="top")

#Creating entry for the calculator, within the input frame.
input_field=tk.Entry(input_frame, font=("arial", 18, "bold"), textvariable=input_text, width=50, bg="#eee", bd=0, justify="right")

#Using the grid layout manager for precise positioning
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


#Next we are establish the second frame, button frame.
#This frame will hold all the buttons in our calculator program
btns_frame=tk.Frame(main_window, width=312, height=272.5, bg="grey")
#Pack the button frame
btns_frame.pack()

#Row 0 holds the clear button and the divide button.
#The clear button clears the screen.  The command paramater calls the btn_clear function which
#handles this
btn_clearing=tk.Button(btns_frame, text="Clear", fg="black",width=32, height=3, bd=0, bg="#eee",
        cursor="hand2", command=btn_clear)

#Using grid layout manager
btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

#The btn_div button is the divide button.  It holds the btn_click command with "/" paramater to allow for division
btn_div=tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bg="#eee",
        cursor="hand2", command=lambda:btn_click("/"))
#Using grid layout manager
btn_div.grid(row=0, column=3, padx=1, pady=1)

#These next 3 buttons are for 7, 8, 9.
#Each one has similar properties.  7, 8 and 9 only differ in two
#ways.  1) the text is different based on number and 2) the command is linked to the respective number
#So when user clicks the button that says 8, python interprets the button to mean the number 8 during calculations
tk.Button(btns_frame, text="7", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="8", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="9", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

#This next button will have the multiply button as the text, and the command will be * for multiply
tk.Button(btns_frame, text="*", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

#These next 3 buttons are for 4, 5, 6.
#Each one has similar properties.  4, 5 and 6 only differ in two
#ways.  1) the text is different based on number and 2) the command is linked to the respective number
#So when user clicks the button that says 6, python interprets the button to mean the number 6 during calculations
tk.Button(btns_frame, text="4", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="5", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="6", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

#This next button will have the minus button as the text, and the command will be - for subtract
tk.Button(btns_frame, text="-", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
#These next 3 buttons are for 1, 2, 3.
#Each one has similar properties.  1, 2 and 3 only differ in two
#ways.  1) the text is different based on number and 2) the command is linked to the respective number
#So when user clicks the button that says 1, python interprets the button to mean the number 1 during calculations
tk.Button(btns_frame, text="1", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

#This next button will have the plus button as the text, and the command will be + for add

tk.Button(btns_frame, text="+", fg="black",width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

#The final row will hold 0, ., =

#The zero button will hold the command parameters to equal zero in value
tk.Button(btns_frame, text="0", fg="black",width=21, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2,padx=1, pady=1)
#The dot button will hold the command parameter to equal the decimal point in value
tk.Button(btns_frame, text=".", fg="black",width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
#The equal button will hold the command parameters of the btn_equal function created earlier in the
#program.  This function evaluates the input numbers and provides result.
tk.Button(btns_frame, text="=", fg="black",width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=btn_equal).grid(row=4, column=3, padx=1, pady=1)



#used for the tkinter library
main_window.mainloop()



