def print_result_set(result_set):
    print_line()
    print_formatted('id', 'title', 'created at', 'status')
    print_line()
    for todo in result_set:
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
