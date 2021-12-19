"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505
Description:
Password manager built using Python

Version: 1.0
"""

import sqlite3

def connectDB():
    """
    This function establishes a connection with the
    master SQLite3 database which consists of all the passwords.
    It will also create a table inside the database which
    will contain all the records.
    """
    global conn, curr
    conn = sqlite3.connect("master.db")
    curr = conn.cursor()

    # Creating a SQL query that will create a table
    # in the database if it does not exists and it will
    # store all the passwords.
    SQL_QUERY = """
    CREATE TABLE IF NOT EXISTS
    PASSWORDS(
        USERNAME CHAR(50),
        PASSWORD CHAR(50),
        WEBSITE CHAR(50),
        USER CHAR(50)
    );
    """

    try:
        curr.execute(SQL_QUERY)   # Executing the command
        conn.commit()
    except sqlite3.Error as er:
        print("Error: ", er)

    return conn, curr