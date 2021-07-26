from models.Todo import Todo
from db.connection import get_connection
from utils.formatter import log, print_result_set


def print_help():
    print("I am the help")


def new_todo(name):
    todo = Todo(title=name)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO todos VALUES(NULL, %s, NOW(), %s)"
    val = (todo.title, todo.status.name)
    cursor.execute(sql, val)

    connection.commit()

    log("Added your todo into the store ... ")


def all_todos():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos")

    result = cursor.fetchall()
    print_result_set(result)


def active_todos():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos WHERE status = 'ACTIVE'")

    result = cursor.fetchall()
    print_result_set(result)


def completed_todos():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos WHERE status = 'COMPLETED'")

    result = cursor.fetchall()
    print_result_set(result)


def today_s_todos():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos WHERE DATE(created_at) = DATE (NOW())")

    result = cursor.fetchall()
    print_result_set(result)


def yesterday_s_todos():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos WHERE DATE(created_at) = DATE (NOW())")

    result = cursor.fetchall()
    print_result_set(result)


def yesterday_but_one_s_todos():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos WHERE DATE(created_at) - DATE (NOW()) = 1")

    result = cursor.fetchall()
    print_result_set(result)
