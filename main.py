import sys

from getopt import getopt, GetoptError
from utils.functions import new_todo, all_todos, print_help


def main(argv):
    try:
        opts, args = getopt(argv, "hi:o:", ["new=", "all"])

        if len(opts) == 0:
            raise GetoptError("")

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                raise GetoptError("")
            elif opt in ('-n', '--new'):
                new_todo(arg)
            elif opt in ('-a', '--all'):
                all_todos()
            else:
                raise GetoptError("")
    except GetoptError:
        print_help()


if __name__ == '__main__':
    main(sys.argv[1:])
