import os,sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

import mysql.connector
from mysql.connector import errorcode
from db import conn_config
from db import sql_clauses

def create_table():
    try:
        # Connection configuration
        config = conn_config.config_db
        # Connect with the MySQL Server
        cnx = mysql.connector.connect(**config)
        # Get buffered cursor
        cursor = cnx.cursor(buffered=True)
        # Query to create users table
        query = sql_clauses.USERS
        # Execute query
        cursor.execute(query)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
