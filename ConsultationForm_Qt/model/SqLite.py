import sqlite3


File = "./database/Consulting.db"


def ConnectDB():
    w = sqlite3.connect(File)
    return w
