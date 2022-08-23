from .Query import Query
from .SqLite import ConnectDB


class QueryDAO:
    def Add(w: Query):
        connect = ConnectDB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Consulting(Name, Email, Telephone, Date, Status, Description) VALUES (?, ?, ?, ?, ?, ?);"
        Dados = [w.Name, w.Email, w.Telephone, w.Date, w.Status, w.Description]
        cursor.execute(SQL, Dados)

        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def EditQueryDAO(w: Query, Id: int):
        connect = ConnectDB()
        cursor = connect.cursor()

        SQL = "UPDATE Consulting SET Name=?, Email=?, Telephone=?, Date=?, Status=?, Description=? WHERE Id=?"
        Dados = [w.Name, w.Email, w.Telephone, w.Date, w.Status, w.Description, Id]
        cursor.execute(SQL, Dados)

        connect.commit()
        connect.close()

    def DeleteQueryDAO(Id: int):
        connect = ConnectDB()
        cursor = connect.cursor()

        SQL = "DELETE FROM Consulting WHERE Id = ?;"
        cursor.execute(SQL, [Id])

        connect.commit()
        connect.close()

    def SelectAll() -> list:
        list_query = []

        connect = ConnectDB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM Consulting;"
        cursor.execute(SQL)
        list = cursor.fetchall()

        for x in list:
            NewQuery = Query(x[0], x[1], x[2], x[3], x[4], x[5], x[6])
            list_query.append(NewQuery)

        connect.close()

        return list_query
