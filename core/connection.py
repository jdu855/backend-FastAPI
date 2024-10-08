import mysql.connector

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'database': 'api',
    'auth_plugin': 'mysql_native_password'
}

def get_connection():
    connection = mysql.connector.connect(**mysql_config)
    return connection

def close_connection(connection):
    connection.close()
