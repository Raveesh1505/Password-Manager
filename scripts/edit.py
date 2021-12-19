"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505
Description:
Password manager built using Python

Version: 1.0
"""

import os
import new
from new import *
import connection
from connection import *

conn, curr = connectDB()

class passwordEdit:
    """
    This class passwordEdit consists of 2 functions
    deletePass and passEdit. This will help in
    executing deletion or editing of a record as
    requested by the user.   
    """

    def deletePass():
        """
        This function will deleter an existing
        record from the database as requested by
        the user.
        """

        print("\nTo delete the record, you will need to enter the webiste and current username of the record you want to delete.\n")
        website = input("Enter the website: ").strip()
        username = input("Enter the current username: ").strip()

        SQL_SYNTAX_1 = """
            SELECT *
            FROM PASSWORDS
            WHERE WEBSITE = ?
            AND USERNAME = ?
            AND USER = ?
            ;
            """

        try:
            curr.execute(SQL_SYNTAX_1, (website, username, new.userID,))
            result = curr.fetchall()
            for column in result:
                print("\nUsername: {}\nPassword: {}\nWebsite: {}\n\n".format(column[0], column[1], column[2]))

            confirmChoice = input("Are you sure you want to delete this record? (y/n): ").lower().strip()
            if confirmChoice == "y":
                SQL_SYNTAX_DELETE = """
                DELETE FROM PASSWORDS
                WHERE WEBSITE = ?
                AND USERNAME = ?
                AND USER = ?
                ;
                """

                try:
                    curr.execute(SQL_SYNTAX_DELETE, (website, username, new.userID,))
                    conn.commit()
                    print("Record deleted succesfully!!!")
                except sqlite3.Error as er:
                    print("Error: ", er)

        except sqlite3.Error as er:
            print("Error: ", er)


    def passEdit():
        """
        This function will perform editing of an
        existing record in the database.
        """
 
        print("\nTo change the details, you will need to enter the webiste and current username of the record you want to change.\n")
        website = input("Enter the website: ").strip()
        username = input("Enter the current username: ").strip()

        SQL_SYNTAX_1 = """
        SELECT *
        FROM PASSWORDS
        WHERE WEBSITE = ?
        AND USERNAME = ?
        AND USER = ?
        ;
        """

        try:
            curr.execute(SQL_SYNTAX_1, (website, username, new.userID,))
            result = curr.fetchall()
            for column in result:
                print("\nUsername: {}\nPassword: {}\nWebsite: {}\n\n".format(column[0], column[1], column[2]))

            changeChoice = ""
                
            while (changeChoice != "9"):
                print("\nWhat do you want to edit\n1. Username\n2. Password.\n3. Website.\nEnter 9 to exit\n\n")
                changeChoice = input("Your choice: ")

                if changeChoice == "1":
                    newUsername = input("Enter the new username: ").strip()
                    SQL_SYNTAX_NU = """
                    UPDATE PASSWORDS
                    SET USERNAME = ?
                    WHERE WEBSITE = ?
                    AND USERNAME = ?
                    AND USER = ?
                    ;
                    """

                    try:
                        curr.execute(SQL_SYNTAX_NU, (newUsername, website, username, new.userID,))
                        conn.commit()
                        print("Record updated successfully!!!")
                    except sqlite3.Error as er:
                        print("Error: ", er)
                    
                elif changeChoice == "2":
                    newPassword = input("Enter the new password: ").strip()
                    SQL_SYNTAX_NU = """
                    UPDATE PASSWORDS
                    SET PASSWORD = ?
                    WHERE WEBSITE = ?
                    AND USERNAME = ?
                    AND USER = ?
                    ;
                    """

                    try:
                        curr.execute(SQL_SYNTAX_NU, (newPassword, website, username, new.userID,))
                        conn.commit()
                        print("Record updated successfully!!!")
                    except sqlite3.Error as er:
                        print("Error: ", er)

                elif changeChoice == "3":
                    newWebsite = input("Enter the new website name: ").strip()
                    SQL_SYNTAX_NU = """
                    UPDATE PASSWORDS
                    SET WEBSITE = ?
                    WHERE WEBSITE = ?
                    AND USERNAME = ?
                    AND USER = ?
                    ;
                    """

                    try:
                        curr.execute(SQL_SYNTAX_NU, (newWebsite, website, username, new.userID,))
                        conn.commit()
                        print("Record updated successfully!!!")
                    except sqlite3.Error as er:
                        print("Error: ", er)        

        except sqlite3.Error as er:
            print("Error: ", er)