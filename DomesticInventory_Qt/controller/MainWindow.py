from PyQt6.QtWidgets import QMainWindow, QHeaderView
from PyQt6 import uic

File_Qt = "view/Home.ui"


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

    def Add(self):
        Name = self.InputName.text()
        Room = self.InputRoom.text()
        Description = self.InputDescription.text()
        Brand = self.InputBrand.text()
        Date = self.InputDate.text()
        Price = self.InputPrice.text()
        Serie = self.InputSerie.text()

    def Update(self):
        pass

    def Delete(self):
        pass
