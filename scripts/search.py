"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505
Description:
Password manager built using Python

Version: 1.0
"""

import os
import pandas as pd
from pandas.core.frame import DataFrame
import new
from new import *
import connection
from connection import *

conn, curr = connectDB()

class passwordExtraction:
    """
    This class passwordExtraction will contain two functions
    named printCSV and releasePass respectively. These two 
    functions will help in the extraction process of all
    passwords securely.
    """

    def printCSV(userID):
        """
        This function prints all the passwords of a user into
        a CSV file and saves it.
        """

        # Contructing a SQL query that will extract all the 
        # saved passwords of a person from the database.
        SQL_QUERY = """
        SELECT *
        FROM PASSWORDS
        WHERE USER = ?
        ;
        """

        try:
            curr.execute(SQL_QUERY, (userID,))    # Extracting the result
            result = curr.fetchall()
            resultDF = DataFrame(result)    # Converting to a Pandas dataframe
            fileName = userID + "_passwords.csv"  # Building a suitable filename
            resultDF.to_csv(fileName)   # Printing the file
            print("File saved succefully!!!")
            
        except sqlite3.Error as er:
            print("Error: ", er)
        

    def releasePass():
        """
        This function will print the password as
        requested by the user.
        """

        print("=====PASSWORD EXTRACTION PORTAL=====")
        print("\n1. Print all passwords.\n2. Filter passwords using webiste.\n3. Filter password using the username.\n4. Print passwords to a spreadsheet.\n\n")
        userChoice = input("Enter your choice: ").strip()

        # Printing all the passwords for the logged in user
        if userChoice == "1":
            SQL_QUERY = """
            SELECT *
            FROM PASSWORDS
            WHERE USER = ?
            ;
            """
            try:
                curr.execute(SQL_QUERY, (new.userID,))
                result = curr.fetchall()
                for column in result:
                    print("\nUsername: {}\nPassword: {}\nWebsite: {}\n\n".format(column[0], column[1], column[2]))
            except sqlite3.Error as er:
                print("Error: ", er)

        # Printing all the passwords filtered using website
        elif userChoice == "2":
            SQL_QUERY = """
            SELECT *
            FROM PASSWORDS
            WHERE USER = ?
            AND WEBSITE = ?
            ;
            """
            userWebsite = input("Enter the website: ").strip()  # Taking website name as user input

            try:
                curr.execute(SQL_QUERY, (new.userID, userWebsite,))
                result = curr.fetchall()
                for column in result:
                    print("\nUsername: {}\nPassword: {}\nWebsite: {}\n\n".format(column[0], column[1], column[2]))
            except sqlite3.Error as er:
                print("Error: ", er)

        # Printing all the passwords filtered using website
        elif userChoice == "3":
            SQL_QUERY = """
            SELECT *
            FROM PASSWORDS
            WHERE USER = ?
            AND USERNAME = ?
            ;
            """
            usernameReg = input("Enter username: ").strip()  # Taking registered username as user input

            try:
                curr.execute(SQL_QUERY, (new.userID, usernameReg,))
                result = curr.fetchall()
                for column in result:
                    print("\nUsername: {}\nPassword: {}\nWebsite: {}\n\n".format(column[0], column[1], column[2]))
            except sqlite3.Error as er:
                print("Error: ", er)

        elif userChoice == "4":
            passwordExtraction.printCSV(new.userID)