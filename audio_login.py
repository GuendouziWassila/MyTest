# contains login function

import tkinter as tk
from tkinter import *

# modify the main window to accept the login password
def login(self):
    
    # destroy the buttons and Title
    self.heading_label.destroy()
    self.login_button.destroy()
    self.create_acct_button.destroy()
    self.quit_button.destroy()

    for r in range(8):
        self.main_win.rowconfigure(r, minsize=20)

    for c in range(6):
        self.main_win.columnconfigure(c, minsize=10)
        
    self.main_win.columnconfigure(0, minsize=50)
    self.main_win.columnconfigure(1, minsize=80)
    self.main_win.columnconfigure(2, minsize=40)
    self.main_win.columnconfigure(3, minsize=40)
    
    
    # Create the entry widgets for user name and password
    self.userName_label = tk.Label(text='User Name: ',\
                                        justify='right',font=("Helvetica",10))
    self.userName_label.grid(row=3,column=2, sticky=E)

    self.user_entry = tk.Entry(width = 18, justify='right', font=("Helvetica",10))
    self.user_entry.grid(row=3, column=3)
    self.user_entry.focus_force()
    

    self.password_label = tk.Label(text='Password: ',\
                                        justify='right',font=("Helvetica",10))
    self.password_label.grid(row=5,column=2, sticky=E)

    self.password_entry = tk.Entry(width = 18, justify='right', font=("Helvetica",10))
    self.password_entry.grid(row=5, column=3)

    
    self.password_entry.bind('<Return>', self.verify_account)              # bind it to the enter key

    self.instruct_label = tk.Label(text='Enter the user name and password and press Enter.')
    self.instruct_label.grid(row=7,column=2, columnspan=3)



