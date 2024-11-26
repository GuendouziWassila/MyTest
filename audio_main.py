# The Audio program

import audio_create_acct
import audio_login
import winsound
import matplotlib.pyplot as plt

import numpy as np
#import scipy
#from scipy import signal
#from scipy.io import wavfile as wav

import wave, sys

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class AudioGUI:
    def __init__(self):
        
        # create the main window
        self.main_win = tk.Tk()
        self.main_win.title("Audio Frequency Program")
        self.main_win.minsize(width=550,height=200)   # set the window size


        for c in range(5):
            self.main_win.columnconfigure(c, minsize=60)
            

        self.main_win.rowconfigure(1, minsize = 50)
        self.main_win.rowconfigure(3, minsize = 250)
        self.main_win.rowconfigure(4, minsize = 30)
        self.main_win.rowconfigure(5, minsize = 30)
        self.main_win.rowconfigure(6, minsize = 30)
        

        # get the image
        photo = PhotoImage(file= "AudioMainArt.gif")
        self.labelGIF = tk.Label(image= photo)
        self.labelGIF.image = photo     # retain a reference
        self.labelGIF.grid(row=3, column=1, columnspan=3)


        
        self.heading_label = tk.Label(text='Audio Frequency Player', \
                                           font=("Helvetica",16), fg="blue")
        self.heading_label.grid(row=1,column=1,columnspan=2,rowspan=2, sticky=E)
        


        # Button - create the button widgets and label for the bottom frame
        self.login_button = tk.Button(text=' User Login ', font=("Helvetica",10), \
                                          command= self.call_login)
        self.login_button.grid(row=5,column=1)

        self.create_acct_button = tk.Button(text=' Create Account ', width=18, font=("Helvetica",10),\
                                            command=self.create_account)        
        self.create_acct_button.grid(row=5,column=2) 
        
        self.quit_button = tk.Button(text='   Cancel   ', font=("Helvetica",10), \
                                          command=self.main_win.destroy)
        self.quit_button.grid(row=5,column=3)


        # Enter the tkinter main loop
        tk.mainloop()


        
    # Create the password creation window and retrieve the data from the text box and process data
    def create_account(self):
        print('Inside create_account and creating the GUI')     # TEST
        #self.labelGIF.destroy()
        CreateAcctWin = audio_create_acct.AccountGUI()    # create the user name request
        CreateAcctWin.account_window.wait_window()

        self.create_acct_button.config(state = DISABLED)    # maybe no reason to do this
        self.login_button.config(state = NORMAL)
         


    def call_login(self):
        # this is done in two steps because calling directly from the button does not allow
        # the login function in the file to access the button.config...self.login_button.config(state = DISABLED)  # disable the login button
        self.labelGIF.destroy()
        audio_login.login(self)   # call the function in data_login.py
        

    # this is called from the ENTER key on the login window
    # verifies the user account
    def verify_account(self,event):
        print('Now in verify      >>>>>>>>>>>>>>..')
        validUser = False
        validPassword = False
        counter = 0
        slot = 0
        userName = self.user_entry.get()        # get the entry
        userPassword = self.password_entry.get()
            
        try:
            userNameFile = open('acct_user_names.txt', 'r')   # try opening the file to read

            # loop line by line to check the values
            for userTemp in userNameFile:
                print('userTemp is ' + userTemp + ' and userName is ' + userName + '\n')
                print('slot is now ' + str(slot) + ' and counter is ' + str(counter) + '\n')
                if userName == userTemp.rstrip():
                    validUser = True
                    slot = counter
                else:
                    counter = counter + 1
                                    
            print('AFTER LOOP  slot is now ' + str(slot) + ' and counter is ' + str(counter) + '\n')
            userNameFile.close()

            print('valid user is now ' + str(validUser))

            if (validUser == True):   # if it exists in the file
                passwordFile = open('acct_user_passwords.txt', 'r')   # open the password file to read

                filePassword = ''   # must be declared outside loop

                for x in range(slot + 1):        # read up to the (but not including) counter number
                    filePassword = passwordFile.readline()
                    print('\n filePassword is now ' + filePassword)

                passwordFile.close()

                if userPassword == filePassword.rstrip():    # check that one
                    validPassword = True
                    print('\n THE PASSWORD MATCHES ')

            if validUser == True and validPassword == True:
                tk.messagebox.showinfo('Good account .......', 'Login Successful.')
                self.show_main()
            else:
                tk.messagebox.showinfo('Invalid Account','Account does not exist.')


        except IOError:
            print('No File exists.')




    # called by verify_account
    def show_main(self):
        print('In show Main now.')

        # destroy the widgets from login
        self.userName_label.destroy()
        self.user_entry.destroy() 
        self.password_label.destroy()
        self.password_entry.destroy()
        self.instruct_label.destroy()

        self.audio_file = ""

        
        for c in range(5):
            self.main_win.columnconfigure(c, minsize=60)

        for r in range(12):
            self.main_win.rowconfigure(r, minsize=30)

        self.main_win.rowconfigure(0, minsize=10)
        self.main_win.rowconfigure(1, minsize=10)
        self.main_win.rowconfigure(2, minsize=20)
        self.main_win.rowconfigure(3, minsize=300)

                
        # get the image
        photo = PhotoImage(file= "AudioMainArt.gif")
        self.labelGIF = tk.Label(image= photo)
        self.labelGIF.image = photo     # retain a reference
        self.labelGIF.grid(row=3, column=1, columnspan=3)

        self.enterFr_button = tk.Button(text='Enter a Frequency', width=18, font=("Helvetica",12),\
                                            command=self.get_user_frequency)        
        self.enterFr_button.grid(row=5, column=1)

        self.plotAmp_button = tk.Button(text='Plot Amplitude', width=18, font=("Helvetica",12),\
                                            command=self.plot_amplitude)        
        self.plotAmp_button.grid(row=7, column=1)

        self.playTone_button = tk.Button(text='Play Audio Tone', width=18, font=("Helvetica",12),\
                                            command=self.play_tone)        
        self.playTone_button.grid(row=9, column=2)

        self.selectFile_button = tk.Button(text='Select Wave File', width=18, font=("Helvetica",12),\
                                            command=self.get_freq_file)        
        self.selectFile_button.grid(row=5, column=3)

        self.plotFreq_button = tk.Button(text='Plot Frequency', width=18, font=("Helvetica",12),\
                                            command=self.plot_frequency)        
        self.plotFreq_button.grid(row=7, column=3)




    def get_user_frequency(self):
        print('Inside get freq function')
        self.freq_entry = tk.Entry(width = 18, justify='right', \
                                   font=("Helvetica",10))
        self.freq_entry.grid(row=5, column=2)
        self.freq_entry.focus_force()
        self.freq_entry.bind('<Return>', self.play_entered_freq)
        self.enter_freq_label = tk.Label(text='Enter and press enter', \
                                           font=("Helvetica",12), fg="blue")
        self.enter_freq_label.grid(row=6,column=2)
        
        print('\n')


    def play_entered_freq(self,event):
        userFreq = int(self.freq_entry.get())        # get the entry
        print(userFreq)
        winsound.Beep(userFreq,1000)    # play the tone
        


    def get_freq_file(self):
        file_path = filedialog.askopenfilename(title='Choose a File')
        self.audio_file = file_path


    def play_tone(self):
        winsound.PlaySound(self.audio_file,winsound.SND_FILENAME)
        


    def plot_amplitude(self):
        print('Inside plot amp function')        
        #***print('\n')
       # all_data = wav.read(self.audio_file)
       # audio = all_data[1]
        #plot the first 1024 samples

       # plt.plot(audio[0:1024])

        #plt.ylabel("Amplitude")
       # plt.xlabel("Time")
        #plt.title(str(self.audio_file))
       # plt.show()
        


    def plot_frequency(self):
        #data = wav.read(self.audio_file)
        #audio = all_data[1]
        #plot the first 1024 samples
        #plt.plot(audio[0:1024])
        #plt.ylabel("Rate")
        #plt.xlabel("1024 Samples")
        #plt.title(str(self.audio_file))
        #plt.show()


        # Load the data and calculate the time of each sample
        raw = wave.open(self.audio_file)
        signal = raw.readframes(1024)   # was -1) which reads all
        signal = np.frombuffer(signal, dtype="int16")

        f_rate = raw.getframerate()

        time = np.linspace(0, len(signal)/f_rate, num = len(signal))
        plt.figure(1)
        plt.title("Wave File")
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.plot(time, signal)
        # You can set the format by changing the extension
        # like .pdf, .svg, .eps
        #plt.savefig('plot.png', dpi=100)
        plt.show()
        

        

# create an instance of the class
audioProject = AudioGUI()
