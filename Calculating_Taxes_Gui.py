#Tax Problem - Our Code:


import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("400x400")  # Corrected
        self.main_window.title("tk")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)


        self.label1_Propertyvalue = tkinter.Label(self.frame1, text="Enter the property value: ")
        self.entry1 = tkinter.Entry(self.frame1, width=10)

        self.label1_Propertyvalue.pack(side="left")
        self.entry1.pack(side="left")




        self.assessment_value = tkinter.StringVar()
        self.property_tax = tkinter.StringVar()

        self.label2_Assessmentvalue = tkinter.Label(self.frame2, text="Assessment Value: ")
        self.assessment_label = tkinter.Label(self.frame2, textvariable=self.assessment_value)

        self.label3_propertytax = tkinter.Label(self.frame3, text="Property Tax: ")
        self.tax_label = tkinter.Label(self.frame3, textvariable=self.property_tax)

        self.label2_Assessmentvalue.pack(side="left")
        self.assessment_label.pack(side="left")
        self.label3_propertytax.pack(side="left")
        self.tax_label.pack(side="left")

        self.calculate_button=tkinter.Button(self.frame4, text="Calculate", command=self.calc_value)
        self.quit_button = tkinter.Button(self.frame4, text='Quit', command=self.main_window.destroy)

        self.calculate_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()


        self.main_window.mainloop()  # Corrected

    def calc_value(self):
        entry1 = float(self.entry1.get())
        assessment_equation=entry1*.60
        propetytax_equation=assessment_equation*.0075
        self.assessment_value.set(f"${assessment_equation:,.2f}")
        self.property_tax.set(f"${propetytax_equation:,.2f}")


MyGUI()



#Time zone problem: Our code:
