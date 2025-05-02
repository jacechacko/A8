#Tax Problem 

#import the GUI library tkinter, and message box if needed.
import tkinter
import tkinter.messagebox
#creates a class MyGUI because we are doing OOP
class MyGUI:
    def __init__(self):
        #creates the main window via tkinter, with the dimensions set with .geometry method and title with .title method
        self.main_window = tkinter.Tk()
        self.main_window.geometry("400x400")  
        self.main_window.title("tk")

        #sets the frames for the program, called frames 1-4.  
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)

#sets the text of the first label to be "Enter property value: "
        self.label1_Propertyvalue = tkinter.Label(self.frame1, text="Enter the property value: ")
        #Provides the entry for the property value
        self.entry1 = tkinter.Entry(self.frame1, width=10)

        #packs the label and entry
        self.label1_Propertyvalue.pack(side="left")
        self.entry1.pack(side="left")



        #stringvar dynamically changes as program applies new logc, for both as. value and propety tax
        self.assessment_value = tkinter.StringVar()
        self.property_tax = tkinter.StringVar()

        #sets label for as, value, text=as. value: 
        self.label2_Assessmentvalue = tkinter.Label(self.frame2, text="Assessment Value: ")
        self.assessment_label = tkinter.Label(self.frame2, textvariable=self.assessment_value)

        #next label, text=Property tax: 
        self.label3_propertytax = tkinter.Label(self.frame3, text="Property Tax: ")
        self.tax_label = tkinter.Label(self.frame3, textvariable=self.property_tax)

        #packs the second label, the third label, tax label, as. label
        self.label2_Assessmentvalue.pack(side="left")
        self.assessment_label.pack(side="left")
        self.label3_propertytax.pack(side="left")
        self.tax_label.pack(side="left")

        #creates a button called calulate, set in frame 4, whose command is the calc_value function we will create later
        self.calculate_button=tkinter.Button(self.frame4, text="Calculate", command=self.calc_value)
        #quit button uses the .destroy method to exit program
        self.quit_button = tkinter.Button(self.frame4, text='Quit', command=self.main_window.destroy)

        #packs the calculate button
        self.calculate_button.pack(side="left")
        #packs the quit button
        self.quit_button.pack(side="left")

        #packs all the frames

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

#this line is required to make the GUI work
        self.main_window.mainloop()  

    #create a function called calc_value, which creates the logic for the "calculate" button
    def calc_value(self):
        #the entry is defined by whatever user put for entry1
        entry1 = float(self.entry1.get())
        #converts the number by multiplying it by 60%
        assessment_equation=entry1*.60
        #then multiplies that by .0075
        propetytax_equation=assessment_equation*.0075
        #sets new values.
        self.assessment_value.set(f"${assessment_equation:,.2f}")
        self.property_tax.set(f"${propetytax_equation:,.2f}")


MyGUI()


