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
    print("=====PASSWORD MANAGER=====\n\n1. Setup new user.\n2. Login.\n")
    userChoice = input("Your choice: ").strip()

    if userChoice == "1":
        masterSetup.newUser()
    
    elif userChoice == "2":
        
        check = masterSetup.masterLogin()

        if check == True:
            print("1. Add a new password\n2. Password search\n3.Password edit\n4. Delete existing password\n")

            loginChoice = input("Your choice: ").strip()

            if loginChoice == "1":
                addData()
            elif loginChoice == "2":
                passwordExtraction.releasePass()
            elif loginChoice == "3":
                passwordEdit.passEdit()
            elif loginChoice == "4":
                passwordEdit.deletePass()
            else:
                print("Invalid input")
        else:
            print("Invalid username or PIN.")
    else:
        print("Invalid input")