from mysql.connector import connect


def get_connection():
    connection = connect(host='localhost', database='task_pad', user='root', password='Rca@{123}')
    return connection


def get_cursor ():
    connection = get_connection()
    return connection.cursor()
