from PyQt6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem
from PyQt6 import uic
from model.Query import Query, EditQuery
from model.Query_dao import QueryDAO

File_Qt = "view/Dash.ui"


def ClearField(self):
    self.Name.clear()
    self.Email.clear()
    self.Telephone.clear()
    self.Description.clear()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.BtnAdd.clicked.connect(self.Add)
        self.BtnEdit.clicked.connect(self.Edit)
        self.BtnDelete.clicked.connect(self.Delete)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.LoadData()

    def LoadData(self):
        list = QueryDAO.SelectAll()
        for x in list:
            self.AddTableWidget(x)

    def Add(self):
        Name = self.Name.text()
        Email = self.Email.text()
        Telephone = self.Telephone.text()
        Date = self.Date.text()
        Status = self.Status.currentText()
        Description = self.Description.text()

        NewQuery = Query(-1, Name, Email, Telephone, Date, Status, Description)

        Id = QueryDAO.Add(NewQuery)
        NewQuery.Id = Id

        self.AddTableWidget(NewQuery)

        ClearField(self)

    def Edit(self):
        Line = self.Table.currentRow()
        LineId = self.Table.item(Line, 0)

        Id = LineId.text()
        Name = self.Name.text()
        Email = self.Email.text()
        Telephone = self.Telephone.text()
        Date = self.Date.text()
        Status = self.Status.currentText()
        Description = self.Description.text()

        Edit = Query(-1, Name, Email, Telephone, Date, Status, Description)
        self.Edition(Edit)
        QueryDAO.EditQueryDAO(Edit, int(Id))

        ClearField(self)

    def Edition(self, w: EditQuery):
        Line = self.Table.currentRow()

        Name = QTableWidgetItem(w.Name)
        Email = QTableWidgetItem(w.Email)
        Telephone = QTableWidgetItem(w.Telephone)
        Date = QTableWidgetItem(w.Date)
        Status = QTableWidgetItem(w.Status)
        Description = QTableWidgetItem(w.Description)

        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Email)
        self.Table.setItem(Line, 3, Telephone)
        self.Table.setItem(Line, 4, Date)
        self.Table.setItem(Line, 5, Status)
        self.Table.setItem(Line, 6, Description)

        ClearField(self)

    def Delete(self):
        Line = self.Table.currentRow()

        LineId = self.Table.item(Line, 0)
        Id = LineId.text()
        self.Table.removeRow(Line)

        QueryDAO.DeleteQueryDAO(int(Id))

    def AddTableWidget(self, w: Query):
        # Define Id do item a ser inserido na tabela
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        # Cria coluna para cada item
        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Email = QTableWidgetItem(w.Email)
        Telephone = QTableWidgetItem(w.Telephone)
        Date = QTableWidgetItem(w.Date)
        Status = QTableWidgetItem(w.Status)
        Description = QTableWidgetItem(w.Description)

        # Adicoina itens na tabela
        self.Table.setItem(Line, 0, Id)
        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Email)
        self.Table.setItem(Line, 3, Telephone)
        self.Table.setItem(Line, 4, Date)
        self.Table.setItem(Line, 5, Status)
        self.Table.setItem(Line, 6, Description)
