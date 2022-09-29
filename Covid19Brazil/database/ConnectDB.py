import sqlite3


File = "./database/Covid19Brazil.db"


def ConnectDB():
    w = sqlite3.connect(File)
    return w
