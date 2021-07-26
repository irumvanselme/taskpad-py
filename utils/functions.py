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
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos")

    result = cursor.fetchall()
    print_line()
    print_formatted('id', 'title', 'created at', 'status')
    print_line()
    for todo in result:
        print_formatted(todo[0], todo[1], str(todo[2]), todo[3])

    print_line()


def log(message, success=True):
    if success:
        print("[SUCCESS]:", message)
    else:
        print("[FAILURE]:", message)


def print_line():
    print("+------+--------------------------------+----------------------+------------+")


def print_formatted(_id, name, created_at, status):
    print("| {:<4} | {:<30} | {:<20} | {:<10} |".format(_id, name, str(created_at), status))
