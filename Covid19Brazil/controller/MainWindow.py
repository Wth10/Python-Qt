from random import randint
from PyQt6.QtWidgets import QMainWindow, QHeaderView

from PyQt6 import uic
from API.ConnectAPI import API

from controller.CardCountry import CardCountry
from model.CardCountry import Country
from model.Covid19Brazil import Covid19Brazil as CVB19
from model.Covid19Brazil_DAO import Covid19Brazil_DAO as CVB19_DAO

File_Qt = "view/Home.ui"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.showMaximized()

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.UpdateAPI.clicked.connect(self.UpdateDataCovid)

    def UpdateDataCovid(self):
        self.ClearCard()

        for x in range(5):
            w = Country(
                f"País {x}",
                randint(1, 99),
                randint(1, 99),
                randint(1, 99),
                randint(1, 99),
                "2020-03-18T23:00:00.000Z",
            )

            Card = CardCountry(w)
            self.CardConteiner.addWidget(Card)

        self.Table.clear()

    def ClearCard(self):
        for x in range(self.CardConteiner.count()):
            Card = self.CardConteiner.itemAt(x).widget()
            Card.hide()
