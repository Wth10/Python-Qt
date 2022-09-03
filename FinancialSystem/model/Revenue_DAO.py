from .Revenue import Revenue
from database.Connect import ConnectDB as DB


class Revenue_DAO:
    def AddDAO(w: Revenue):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Receita(Description, Price) VALUES (?, ?);"
        Dados = [w.Description, w.Price]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def EditDAO(w: Revenue, Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "UPDATE Receita SET Description=?, Price=? WHERE Id=?"
        Dados = [w.Description, w.Price, Id]

        cursor.execute(SQL, Dados)
        connect.commit()
        connect.close()

    def DeleteDAO(Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "DELETE FROM Receita WHERE Id = ?;"
        cursor.execute(SQL, [Id])

        connect.commit()
        connect.close()

    def SelectAll() -> list:
        Finance_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM Receita;"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = Revenue(x[0], x[1], x[2])
            Finance_List.append(w)
        connect.close()

        return Finance_List
