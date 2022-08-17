from PyQt6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem
from PyQt6 import uic
from model.Domestic_Inventory import Domestic_Inventory, EditDomestic_Inventory
from model.Domestic_Inventory_DAO import Domestic_Inventory_DAO

File_Qt = "view/Home.ui"


def ClearField(self):
    self.InputName.clear()
    self.InputRoom.clear()
    self.InputDescription.clear()
    self.InputBrand.clear()
    self.InputPrice.clear()
    self.InputSerie.clear()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.BtnAdd.clicked.connect(self.Add)
        self.BtnUpdate.clicked.connect(self.Update)
        self.BtnDelete.clicked.connect(self.Delete)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.LoadData()
        self.Alert()

    def LoadData(self):
        list = Domestic_Inventory_DAO.SelectAll()
        for x in list:
            self.AddTableWidget(x)

    def Add(self):
        Name = self.InputName.text()
        Room = self.InputRoom.text()
        Description = self.InputDescription.text()
        Brand = self.InputBrand.text()
        Date = self.InputDate.text()
        Price = self.InputPrice.text()
        Serie = self.InputSerie.text()

        New = Domestic_Inventory(-1, Name, Room, Description, Brand, Date, Price, Serie)

        Id = Domestic_Inventory_DAO.Add(New)
        New.Id = Id
        self.AddTableWidget(New)
        ClearField(self)
        self.Alert()

    def Alert(self):
        Price = Domestic_Inventory_DAO.CountItens()
        self.AlertValueTotal.setText(format(f"R$ {Price}"))
        self.AlertTotalItens.setText(str(self.Table.rowCount()))

    def Update(self):
        Line = self.Table.currentRow()
        LineId = self.Table.item(Line, 0)

        Id = LineId.text()
        Name = self.InputName.text()
        Room = self.InputRoom.text()
        Description = self.InputDescription.text()
        Brand = self.InputBrand.text()
        Date = self.InputDate.text()
        Price = self.InputPrice.text()
        Serie = self.InputSerie.text()

        Update = Domestic_Inventory(
            -1, Name, Room, Description, Brand, Date, Price, Serie
        )

        self.Edition(Update)
        Domestic_Inventory_DAO.EditDAO(Update, int(Id))
        self.Alert()

    def Edition(self, w: EditDomestic_Inventory):
        Line = self.Table.currentRow()

        Name = QTableWidgetItem(w.Name)
        Room = QTableWidgetItem(w.Room)
        Description = QTableWidgetItem(w.Description)
        Brand = QTableWidgetItem(w.Brand)
        Date = QTableWidgetItem(w.Date)
        Price = QTableWidgetItem(f"R$ {w.Price}")
        Serie = QTableWidgetItem(w.Serie)

        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Room)
        self.Table.setItem(Line, 3, Description)
        self.Table.setItem(Line, 4, Brand)
        self.Table.setItem(Line, 5, Date)
        self.Table.setItem(Line, 6, Price)
        self.Table.setItem(Line, 7, Serie)

        ClearField(self)

    def Delete(self):
        Line = self.Table.currentRow()

        LineId = self.Table.item(Line, 0)
        Id = LineId.text()
        self.Table.removeRow(Line)

        Domestic_Inventory_DAO.DeleteDAO(int(Id))
        self.Alert()

    def AddTableWidget(self, w: Domestic_Inventory):
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Room = QTableWidgetItem(w.Room)
        Description = QTableWidgetItem(w.Description)
        Brand = QTableWidgetItem(w.Brand)
        Date = QTableWidgetItem(w.Date)
        Price = QTableWidgetItem(f"R$ {w.Price}")
        Serie = QTableWidgetItem(w.Serie)

        self.Table.setItem(Line, 0, Id)
        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Room)
        self.Table.setItem(Line, 3, Description)
        self.Table.setItem(Line, 4, Brand)
        self.Table.setItem(Line, 5, Date)
        self.Table.setItem(Line, 6, Price)
        self.Table.setItem(Line, 7, Serie)
