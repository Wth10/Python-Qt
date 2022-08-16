import sqlite3


File = ".Home_Inventory.db"


def ConnectDB():
    w = sqlite3.connect(File)
    return w
