from sqlite3 import connect
from .Domestic_Inventory import Domestic_Inventory as Di
from database.ConnectDB import ConnectDB as DB


class Domestic_Inventory_DAO:
    def Add(w: Di):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Domestic_Inventory(Name, Room, Description, Brand, Date, Price, Serie) VALUES (?, ?, ?, ?, ?, ?, ?);"
        Dados = [w.Name, w.Room, w.Description, w.Brand, w.Date, w.Price, w.Serie]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def CountItens():
        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT SUM(Price) FROM Domestic_Inventory"
        PriceX = cursor.execute(SQL)
        Price = PriceX.fetchone()[0]
        connect.close()
        return Price

    def EditDAO(w: Di, Id: int):
        connect = DB()
        cursor = connect.cursor()
        SQL = "UPDATE Domestic_Inventory SET Name=?, Room=?, Description=?, Brand=?, Date=?, Price=?, Serie=? WHERE Id=?"
        Dados = [w.Name, w.Room, w.Description, w.Brand, w.Date, w.Price, w.Serie, Id]
        cursor.execute(SQL, Dados)
        connect.commit()
        connect.close()

    def DeleteDAO(Id: int):
        connect = DB()
        cursor = connect.cursor()
        SQL = "DELETE FROM Domestic_Inventory WHERE Id = ?;"
        cursor.execute(SQL, [Id])
        connect.commit()
        connect.close()

    def SelectAll() -> list:
        list_Inventory = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM Domestic_Inventory;"
        cursor.execute(SQL)
        list = cursor.fetchall()

        for x in list:
            w = Di(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
            list_Inventory.append(w)

        connect.close()

        return list_Inventory
