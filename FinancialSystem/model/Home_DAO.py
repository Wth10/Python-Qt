from database.Connect import ConnectDB as DB


class Home_DAO:
    def CountRevenueDAO():
        connect = DB()
        cursor = connect.cursor()

        SQL = "SELECT SUM(Price) FROM Receita"

        w = cursor.execute(SQL)
        x = w.fetchone()[0]
        connect.close()
        return x

    def CountExpensesDAO():
        connect = DB()
        cursor = connect.cursor()

        SQL = "SELECT SUM(Price) FROM Despesa"

        w = cursor.execute(SQL)
        x = w.fetchone()[0]
        connect.close()
        return x
