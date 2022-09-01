from .Expenses import Expenses
from database.Connect import ConnectDB as DB


class Expenses_DAO:
    def AddDAO(w: Expenses):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Despesa(Description, Price) VALUES (?, ?);"
        Dados = [w.Description, w.Price]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def EditDAO(w: Expenses, Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "UPDATE Despesa SET Description=?, Price=? WHERE Id=?"
        Dados = [w.Description, w.Price, Id]

        cursor.execute(SQL, Dados)
        connect.commit()
        connect.close()

    def DeleteDAO(Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "DELETE FROM Despesa WHERE Id = ?;"
        cursor.execute(SQL, [Id])

        connect.commit()
        connect.close()

    def CountExpensesDAO():
        connect = DB()
        cursor = connect.cursor()

        SQL = "SELECT SUM(Price) FROM Despesa"

        w = cursor.execute(SQL)
        x = w.fetchone()[0]
        connect.close()
        return x

    def SelectAll() -> list:
        Finance_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM Despesa;"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = Expenses(x[0], x[1], x[2])
            Finance_List.append(w)
        connect.close()

        return Finance_List
