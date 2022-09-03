from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt6 import uic

from model.Revenue import Revenue
from model.Revenue_DAO import Revenue_DAO

File_Qt = "view/Receita.ui"


class ControlRevenue(QWidget):
    def __init__(self) -> None:
        super(ControlRevenue, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.BtnSave.clicked.connect(self.RegisterRecipe)
        self.BtnEdit.clicked.connect(self.EditRecipe)
        self.BtnDelete.clicked.connect(self.DeleteRecipe)

        self.LoadData()

    def ClearField(self):
        self.InputDescription.clear()
        self.InputPrice.clear()
        self.AlertErro.clear()

    def LoadData(self):
        list = Revenue_DAO.SelectAll()
        for x in list:
            self.AddTableWidget(x)

    def RegisterRecipe(self):
        Description = self.InputDescription.text()
        Price = self.InputPrice.text()

        if Description == "" or Price == "":
            self.AlertErro.setText(f"Preencha Todos Os Campos")
        else:
            New = Revenue(-1, Description, Price)

            Id = Revenue_DAO.AddDAO(New)
            New.Id = Id
            self.AddTableWidget(New)
            self.ClearField()

    def EditRecipe(self):
        Line = self.Table.currentRow()
        LineId = self.Table.item(Line, 0)

        Id = LineId.text()

        Description = self.InputDescription.text()
        Price = self.InputPrice.text()

        if Description == "" or Price == "":
            self.AlertErro.setText(f"Preencha Todos Os Campos")
        else:
            Update = Revenue(-1, Description, Price)
            self.Edition(Update)
            Revenue_DAO.EditDAO(Update, int(Id))

    def Edition(self, w: Revenue):
        Line = self.Table.currentRow()

        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(f"R$ {w.Price}")
        self.Table.setItem(Line, 1, Description)
        self.Table.setItem(Line, 2, Price)
        self.ClearField()

    def DeleteRecipe(self):
        Line = self.Table.currentRow()

        LineId = self.Table.item(Line, 0)
        Id = LineId.text()
        self.Table.removeRow(Line)

        Revenue_DAO.DeleteDAO(int(Id))

    def AddTableWidget(self, w: Revenue):
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(f"R$ {w.Price}")

        self.Table.setItem(Line, 0, Id)
        self.Table.setItem(Line, 1, Description)
        self.Table.setItem(Line, 2, Price)
