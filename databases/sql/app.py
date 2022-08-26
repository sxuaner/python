#!/Users/xuansong/.bin/miniconda3/envs/sql/bin/python3.8
import sqlite3
from sqlite3 import Error as Err

# explicit function to connect to database
# that resides in the memory
def SQLite_connection():
 
    try:
        # connect to the database
        conn = sqlite3.connect('gfgdatabase.db')
        print("Database connection is established successfully!")
        conn.close()
        # connect a database connection to the
        # mem database 
        conn = sqlite3.connect(':memory:')
        print("Established database connection to a database\
        that resides in the memory!")
        
    # if any interruption or error occurs
    except Err: print(Err)
 
    # terminate the connection   
    finally: conn.close()
         
# function call       
SQLite_connection()