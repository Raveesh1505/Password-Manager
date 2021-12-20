"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505
Description:
Password manager built using Python

Version: 1.0
"""

import os
import connection
from connection import *
from getpass import getpass
from lockfile import LockFile

conn, curr = connectDB()

lock = LockFile("scripts/resources/masterPass.txt.lock")

class masterSetup:
    """
    This class masterSetup will contain of two functions
    named masterRegister and masterLogin respectively.
    These two functions will help in registering and
    login of the master user.
    """

    def newUser():
        """
        This function registeres a new user. It takes
        master username and master PIN of the user and
        saves it into masterPass.txt file.
        """

        masterUserID = input("Enter your master username: ")    # Taking master user ID as input
        masterPIN = input("Enter your master PIN: ")    # Taking master PIN as input
        
        # Both userID and PIN will be converted to binaries and will be stored in txt file
        binUID = ''.join(format(i, '08b') for i in bytearray(masterUserID, encoding ='utf-8'))
        binPIN = ''.join(format(i, '08b') for i in bytearray(masterPIN, encoding ='utf-8'))

        # Printing the details for verification

        print("Please verify the details entered by you\nMaster username: {}\nMaster PIN: {}".format(masterUserID, masterPIN))
        userConfirmation = input("Are the details correct? (y/n): ").lower()

        if userConfirmation == 'y':
            
            with lock:
                # Adding the master login data into the txt file
                passFile = open("scripts/resources/masterPass.txt", "a")  # Opening file in append mode
                content = ["{} {}\n".format(binUID, binPIN)]  # Creating a content string
                passFile.writelines(content)    # Writting the content
                passFile.close()
                lock.acquire()

            print("\nMaster data added succesfully!!!\n")

        else:
            print("Try again\n")
            masterSetup.newUser()


    def masterLogin():
        """
        This function performs the master login task.
        It takes the master userID and masterPin as an
        input from the user and then reads and compares
        from the data stored in masterPass.txt file. 
        """
        global userID  # Globalising the master userID variable for further use
        userID = input("UserID: ").strip()    # Taking input from the user for his/her master userID
        userPIN = getpass(prompt="PIN: ")  # Taking input from the user for his/her master PIN

        # Converting the input to binaries for comparison
        binUID = ''.join(format(i, '08b') for i in bytearray(userID, encoding ='utf-8'))
        binPIN = ''.join(format(i, '08b') for i in bytearray(userPIN, encoding ='utf-8'))

        with lock:
            with open("scripts/resources/masterPass.txt", "r") as f:
                for line in f:
                    a,b = line.split(" ")
                    b = b.strip()
                    a  = a.strip()

                    if (a == binUID and b == binPIN):
                        return True
                    else:
                        return False
                f.close()
                lock.acquire()


def addData():
    """
    This function will take username, password and website
    as input from the user. It will then confirm the details
    entered by the user. If all the details are correct, it
    will return true and function will be considered a success
    else it will restart the function.
    """
    
    username = input("Enter your username: ").strip()   # Taking a new username as input
    password = input("Enter the password: ").strip()    # Taking a new password as input
    website = input("Enter the website: ")  # Taking the website for which the record is being added

    # Printing the details entered by user for confirmation
    print("Please verify the details enterd by you\n\nUsername: {}\nPassword: {}\nWebsite: {}\nUser: {}".format(username, password, website, userID))
    userConfirmation = input("\n\nAre the details correct? (y/n): ").lower()

    if userConfirmation == 'y':
            
        # Constructing a SQL Query that will insert the data
        # into our PASSWORDS table in our SQLITE3 master.db.
        SQL_QUERY = """
        INSERT INTO PASSWORDS
        VALUES (
            ?,
            ?,
            ?,
            ?
        );
        """
        try:    # Executing the query
            curr.execute(SQL_QUERY, (username, password, website, userID))
            conn.commit()
            print("Data added succefully.")
        except sqlite3.Error as er:
            print("Error: ", er)
    else:
        print("Try again\n\n")
        addData()