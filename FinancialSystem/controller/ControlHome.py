from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from model.Home_DAO import Home_DAO
from decimal import Decimal
import locale

File_Qt = "view/Home.ui"


class Home(QWidget):
    def __init__(self) -> None:
        super(Home, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Alert()

    def FormatNumber(self, w):
        locale.setlocale(locale.LC_ALL, "pt_BR")
        x = Decimal(0 if w is None else w)
        a = locale.currency(x, grouping=True)
        return a

    def Alert(self):
        Revenue = Home_DAO.CountRevenueDAO()
        self.LR.setText(f"{self.FormatNumber(Revenue)}")

        Expenses = Home_DAO.CountExpensesDAO()
        self.LD.setText(f"{self.FormatNumber(Expenses)}")

        A = Expenses if Expenses != None else 0
        B = Revenue if Revenue is None else Revenue

        if A == B:
            self.LT.setText(f"😳")
        else:
            self.LT.setText(f"{self.FormatNumber(B - A)}")
