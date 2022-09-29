from .Covid19Brazil import Covid19Brazil as CVB19
from database.ConnectDB import ConnectDB as DB


class Covid19Brazil_DAO:
    def Add(w: CVB19):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Covid19Brazil(uid, uf, state, cases, deaths, suspects, refuses, datetime) VALUES (?,?,?,?,?,?,?,?);"
        Dados = [
            w.uid,
            w.uf,
            w.state,
            w.cases,
            w.deaths,
            w.suspects,
            w.refuses,
            w.datetime,
        ]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id
