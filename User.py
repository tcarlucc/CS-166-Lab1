from enum import Enum

class access_level(Enum):
    BASIC = 1
    ADVANCED = 2
    ADMIN = 3

class User:
    def __init__(self, username, password, access):
        self.username = username
        self.password = password
        self.access = access_level.BASIC # Default value. Can be changed by admin users.

