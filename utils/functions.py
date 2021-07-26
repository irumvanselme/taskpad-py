from models.Todo import Todo
from utils.db.connection import get_connection


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
    print("Showing all todos ")


def log(message, success=True):
    if success:
        print("[SUCCESS]:", message)
    else:
        print("[FAILURE]:", message)
