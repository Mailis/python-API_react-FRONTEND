import mysql.connector
from mysql.connector import errorcode
from db import conn_config
from db import sql_clauses
from auth import password_utils
# import app_configs

class User():
    def __init__(self):
        self.set_up()

    def userExists(self, fullname:str, username:str, phone:str, strict = True):
        # _id, _fullname, _username, _phone = self.get_user_by_fullname(fullname)
        querySucc, userdata = self.get_user_by_fullname(fullname)
        if(querySucc is False):
            return
        # print(userdata)
        userExists = False
        if(len(userdata) > 0):
            _id, _fullname, hashed_username, _phone = userdata
            # print('_fullname ' + _fullname)
            # print('_username ' +  _username)
            # print('_phone ' +  _phone)
            isSame_fullname = fullname == _fullname
            isSame_userame = password_utils.check_if_username_is_safe(username, hashed_username)
            isSame_phone = phone == _phone
            if(strict is True):
                userExists = isSame_fullname or isSame_userame or isSame_phone
            else:
                userExists = isSame_fullname or isSame_userame


        return userExists, userdata
    
        
    def set_up(self):
        # Connection configuration
        self.config = conn_config.config_db
        # Connect with the MySQL Server
        self.cnx = mysql.connector.connect(**self.config)
        # Get buffered cursor
        self.cursor = self.cnx.cursor(buffered=True)
        
    def connectionIsOpen(self):
        if(self.cnx.is_connected()):
            return True
        else:
            return False

    def insert_user(self, fullname:str, username:str, phone:str):
        try:
            userExists, _ = self.userExists(fullname, username, phone, False)
            # user
            if(userExists):
                return False, "User already exists."
            secured_username = password_utils.generate_safe_username(username)
            print('secured_username', secured_username)
            user = (fullname, secured_username, phone)

            # Query to insert a user
            query = sql_clauses.USERS_INSERT
            if(self.connectionIsOpen() is False):
                self.set_up()
            self.cursor.execute(query, user)
            self.cnx.commit()
        except mysql.connector.Error as err:
            self.send_error(err)
            return False, self.send_error(err)
        except Exception as err:
            return False, self.send_error(err)
        else:
            self.cnx.close()
            return True, "OK"


    def delete_user_by_id(self, id:int):
        try:
            # Query to insert a user
            query = sql_clauses.USERS_DELETE_BY_ID

            if(self.connectionIsOpen() is False):
                self.set_up()
            self.cursor.execute(query, (id,))
            self.cnx.commit()

        except mysql.connector.Error as err:
            self.send_error(err)
            return False, self.send_error(err)
        except Exception as err:
            return False, self.send_error(err)
        else:
            self.cnx.close()
            return True, str(id)


    def get_all_users(self):
        result_set = None
        try:
            query = sql_clauses.USERS_SELECT_ALL

            if(self.connectionIsOpen() is False):
                self.set_up()
            self.cursor.execute(query)
            self.cnx.commit()

            if(self.connectionIsOpen() is False):
                self.set_up()
            result_set = self.cursor.fetchall()

            return(True, result_set)
        except mysql.connector.Error as err:
            return False, self.send_error(err)
        except IndexError as err:
            return False, self.send_error(err,  "User with id " + id + " doesn't exist!")
        except Exception as err:
            return False, self.send_error(err)
        else:
            self.cnx.close()
            return True, result_set



    def get_user_by_id(self, id:int):
        result_set = None
        try:
            query = sql_clauses.USERS_SELECT_BY_ID

            if(self.connectionIsOpen() is False):
                self.set_up()
            self.cursor.execute(query, (id,) )
            self.cnx.commit()

            if(self.connectionIsOpen() is False):
                self.set_up()
            result_set = self.cursor.fetchall()

            if(len(result_set) > 0):
                result_set = result_set.pop()
            print(result_set)
        except mysql.connector.Error as err:
            return False, self.send_error(err)
        except IndexError as err:
            return False, self.send_error(err,  "User with id " + id + " doesn't exist!")
        except Exception as err:
            return False, self.send_error(err)
        else:
            self.cnx.close()
            return True, result_set

    
    def get_user_by_fullname(self, fullname:str):
        result_set = None
        try:
            query = sql_clauses.USERS_SELECT_BY_FULLNAME
            if(self.connectionIsOpen() is False):
                self.set_up()
            self.cursor.execute(query, (fullname,) )
            self.cnx.commit()

            if(self.connectionIsOpen() is False):
                self.set_up()
            result_set = self.cursor.fetchall()

            if(len(result_set) > 0):
                result_set = result_set.pop()
            # print(result_set)
        except mysql.connector.Error as err:
            return False, self.send_error(err)
        except IndexError as err:
            return False, self.send_error(err,  "User with id " + id + " doesn't exist!")
        except Exception as err:
            return False, self.send_error(err)
        else:
            self.cnx.close()
            return True, result_set


    def send_error(self, err, err_message = ""):
        if(err_message == ""):
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                err_message = ("Something is wrong with your user name or password. " + err)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                err_message = ("Database does not exist. " + err)
            else:
                err_message = (err)
        else:
            err_message = err_message + " \r\n " + (err)
        return(err_message)
        
        

