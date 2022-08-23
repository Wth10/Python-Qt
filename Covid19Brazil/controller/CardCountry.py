from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from model.CardCountry import Country

File_Qt = "view/CardCountry.ui"


class CardCountry(QWidget):
    def __init__(self, x: Country):
        super(CardCountry, self).__init__()
        uic.loadUi(File_Qt, self)
        self.x = x

        self.Load()

    def Load(self):
        self.Status.setText(f"Status {self.x.Country}")
        self.Confirmed.setText(f"{self.x.Confirmed} Confirmados")
