from pip._internal.utils.misc import enum

status = enum(ACTIBE)

class Todo:
    id = 0
    title = ""
    status = "ACTIVE"


    def __init__(self, title):
        self.title = title
