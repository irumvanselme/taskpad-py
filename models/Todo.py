from utils.enums import TodoStatus
from datetime import datetime


class Todo:
    def __init__(self, title, _id=0, status=TodoStatus.ACTIVE, created_at=datetime.now()):
        self.id = _id
        self.title = title
        self.status = status
        self.created_at = created_at
