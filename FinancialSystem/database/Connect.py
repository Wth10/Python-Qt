import sqlite3


File = "./database/Finance.db"


def ConnectDB():
    w = sqlite3.connect(File)
    return w
