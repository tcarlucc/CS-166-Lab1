from enum import Enum


class AccessLevel(Enum):
    BASIC = 1
    ADVANCED = 2
    ADMIN = 3


class User:
    def __init__(self, username, password, access):
        self.username = username
        self.password = password
        self.access = access

    def __str__(self):
        return(self.username + " "+ self.password)