from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from model.Revenue_DAO import Revenue_DAO
from model.Expenses_DAO import Expenses_DAO

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
        Revenue = Revenue_DAO.CountRevenueDAO()
        self.LR.setText(f"{self.FormatNumber(Revenue)}")

        Expenses = Expenses_DAO.CountExpensesDAO()
        self.LD.setText(f"{self.FormatNumber(Expenses)}")

        self.LT.setText(f"{self.FormatNumber(Revenue - Expenses)}")
