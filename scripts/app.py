"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505
Description:
Password manager built using Python

Version: 1.0
"""

import os
import sqlite3
import edit, new, search
from edit import *
from new import *
from search import *

if __name__ == "__main__":
    
    # Main menu view
    print("=====PASSWORD MANAGER=====\n\n1. Setup new user.\n2. Login.\n") 
    userChoice = input("Your choice: ").strip()
    flag = 0    # If user fails to give correct input, a flag will be raised
    maxFlag = 3 # Maximum available chances

    if userChoice == "1":
        print("\n=====NEW USER REGISTRATION=====\n\n")
        masterSetup.newUser()   # Running new registration script
    
    elif userChoice == "2":
        
        while flag < 3:
            check = masterSetup.masterLogin()   # Running master login script

            while check == True:
                print("\n=====MAIN MENU=====\n\n1. Add a new password\n2. Password search\n3. Password edit\n4. Delete existing password\n")

                loginChoice = input("Your choice: ").strip()

                if loginChoice == "1":
                    print("\n=====NEW PASSWORD ADDITION=====\n\n")
                    addData()   # Running new data addition script
                elif loginChoice == "2":
                    passwordExtraction.releasePass()    # Running password extraction script
                elif loginChoice == "3":
                    print("\n=====EDIT PASSWORDS=====\n\n")
                    passwordEdit.passEdit() # Running password edit script
                elif loginChoice == "4":
                    print("\n=====DELETE PASSWORDS=====\n\n")
                    passwordEdit.deletePass()   # Running password deletion script
                else:
                    print("Invalid input")
            flag += 1
            print("\nWARNING: Invalid username or PIN. Attempts left: {}".format(maxFlag-flag))
        print("\nTIMEOUT: You have reached maximum attempts. Please try again later.")
    else:
        print("Invalid input")