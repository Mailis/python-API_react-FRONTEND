user = 'root'
password = 'maika'
host = '127.0.0.1'
raise_warnings = True
db_name = 'smit'
table_users_name = 'users'


table_users_path = db_name + "." + table_users_name


config_mysql = {
    'user': user,
    'password': password,
    'host': host,
    'raise_on_warnings': raise_warnings,
    }

config_db = {
    'user': user,
    'password': password,
    'host': host,
    'database': db_name,
    'raise_on_warnings': raise_warnings,
    }