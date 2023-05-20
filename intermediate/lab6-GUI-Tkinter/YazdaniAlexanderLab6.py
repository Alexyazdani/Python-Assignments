"""
Please Replace Lab 3

Lab 6: GUI
Alexander Yazdani
CWID: 20399751
Date: 03/21/2023

This file uses the tkinter module to create a class that defines a simple GUI.
The GUI can convert an entry of kilometers into miles.  
The converted value will be displayed in an information dialog box.
The entry is validated to be sure that it is a number and is non-negative.
"""

from tkinter import *
from decimal import Decimal
import tkinter.messagebox

class KM_GUI(Frame):
    """
    Instantiating an object of KM_GUI class and running mainloop() will open a new window that functions as a GUI.
    The GUI allows users to enter a value of kilometers c,onverts to miles, and displays the converted value in an information dialogue box.
    User input is validated when checked.
    """
    def __init__(self, master = None):
        """
        Initialization is based off of __init__ from 'Frame'
        """
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    
    def init_window(self):
        """
        This initialization for the KM_GUI class creates a new window.
        There is a Label for "Kilometers" and a text entry box below.
        Below that is a  utton to convert and a button to quit the window.
        """
        self.master.title("Km to mi Converter")
        self.pack(fill=BOTH, expand=1)
        quit = Button(self, text = "Quit", command=self.exit_application)
        convert = Button(self, text = "Convert", command=self.convert_to_miles)
        convert.place(x = 10, y = 50)
        quit.place(x=100, y=50)
        km_label = Label(self, text = "Kilometers:")
        km_label.place(x = 10, y = 5)
        self.km_entry = Entry(self)
        self.km_entry.place(x = 10, y = 25)

    def exit_application(self):
        """
        This method will close the application.  It is called when the 'Quit' button is pressed.
        """
        exit()
    
    def convert_to_miles(self):
        """
        This method will convert the user's input from kilometers to miles.
        First, user input is validated.
        The value is then converted and displayed in a new information dialogue box.
        """
        try:
            miles = Decimal(self.km_entry.get())*Decimal(0.62137119)
            if miles < 0:
                raise ValueError
            tkinter.messagebox.showinfo("Miles:", f"{round(miles, 2)}")
            return True
        except:
            return False

root = Tk()
root.geometry("150x100")
app = KM_GUI(root)

root.mainloop()
