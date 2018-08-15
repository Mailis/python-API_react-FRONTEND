from . import conn_config

#DATABASE
DATABASE = ("CREATE DATABASE IF NOT EXISTS " + conn_config.db_name)

#TABLES
USERS = ("CREATE TABLE IF NOT EXISTS " + conn_config.table_users_path + " ("
            "id int NOT NULL AUTO_INCREMENT,"
            "fullname varchar(100) NOT NULL,"
            "username varchar(500) NOT NULL,"
            "phone varchar(50) NOT NULL,"
            "PRIMARY KEY (id)"
            ")"
            "ENGINE=InnoDB DEFAULT CHARSET=latin1")

USERS_INSERT = ("INSERT INTO " + conn_config.table_users_path + "(fullname, username, phone)"
               " VALUES (%s, %s, %s)")

USERS_SELECT_ALL = ("SELECT * FROM " + conn_config.table_users_path)
USERS_SELECT_BY_ID = ("SELECT * FROM " + conn_config.table_users_path + " WHERE id = %s")
USERS_SELECT_BY_FULLNAME = ("SELECT * FROM " + conn_config.table_users_path + " WHERE fullname = %s")

USERS_DELETE_BY_ID = ("DELETE FROM " + conn_config.table_users_path + " WHERE id = %s")