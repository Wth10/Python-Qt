from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt6 import uic

from model.Expenses import Expenses
from model.Expenses_DAO import Expenses_DAO

File_Qt = "view/Despesa.ui"


def ClearField(self):
    self.InputDescription.clear()


class ControlExpenses(QWidget):
    def __init__(self) -> None:
        super(ControlExpenses, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.BtnSave.clicked.connect(self.RegisterExpenses)
        self.BtnEdit.clicked.connect(self.EditExpenses)
        self.BtnDelete.clicked.connect(self.DeleteExpenses)

        self.LoadData()

    def LoadData(self):
        list = Expenses_DAO.SelectAll()
        for x in list:
            self.AddTableWidget(x)

    def RegisterExpenses(self):
        Description = self.InputDescription.text()
        Price = self.InputPrice.text()

        New = Expenses(-1, Description, Price)

        Id = Expenses_DAO.AddDAO(New)
        New.Id = Id
        self.AddTableWidget(New)
        ClearField(self)

    def EditExpenses(self):
        Line = self.Table.currentRow()
        LineId = self.Table.item(Line, 0)

        Id = LineId.text()
        Description = self.InputDescription.text()
        Price = self.InputPrice.text()

        Update = Expenses(-1, Description, Price)

        self.Edition(Update)
        Expenses_DAO.EditDAO(Update, int(Id))

    def Edition(self, w: Expenses):
        Line = self.Table.currentRow()

        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(f"R$ {w.Price}")

        self.Table.setItem(Line, 1, Description)
        self.Table.setItem(Line, 2, Price)

        ClearField(self)

    def DeleteExpenses(self):
        Line = self.Table.currentRow()

        LineId = self.Table.item(Line, 0)
        Id = LineId.text()
        self.Table.removeRow(Line)

        Expenses_DAO.DeleteDAO(int(Id))

    def AddTableWidget(self, w: Expenses):
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(f"R$ {w.Price}")

        self.Table.setItem(Line, 0, Id)
        self.Table.setItem(Line, 1, Description)
        self.Table.setItem(Line, 2, Price)
