import mysql.connector

if __name__ == '__main__':
    connection = mysql.connector.connect(host='localhost', database='task_pad', user='root', password='Rca@{123}')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select * from todos")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
