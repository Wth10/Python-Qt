from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from controller.ControlHome import Home
from controller.ControlRevenue import ControlRevenue
from controller.ControlExpenses import ControlExpenses

from theme.AppTheme import DARK, LIGHT

File_Qt = "view/Dashboard.ui"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.setWindowTitle("Finance")
        self.showMaximized()

        # Cria os objetos das páginas
        self.PagHome = Home()
        self.PagRevenue = ControlRevenue()
        self.PagExpenses = ControlExpenses()

        # Insere as páginas
        self.StackedWidget.addWidget(self.PagHome)
        self.StackedWidget.addWidget(self.PagRevenue)
        self.StackedWidget.addWidget(self.PagExpenses)

        # Ações dos botões
        self.BtnHome.clicked.connect(self.ActionMenu)
        self.BtnRevenue.clicked.connect(self.ActionMenu)
        self.BtnExpense.clicked.connect(self.ActionMenu)
        self.BtnTheme.clicked.connect(self.ActionMenu)

        self.setStyleSheet(DARK)

    def ActionMenu(self):
        Button = self.sender()
        ClickedButton = Button.objectName()

        if ClickedButton == "BtnHome":
            self.StackedWidget.setCurrentIndex(0)

        if ClickedButton == "BtnRevenue":
            self.StackedWidget.setCurrentIndex(1)

        if ClickedButton == "BtnExpense":
            self.StackedWidget.setCurrentIndex(2)

        if ClickedButton == "BtnTheme":
            self.CheckButton()

    def CheckButton(self):
        if self.BtnTheme.isChecked():
            self.setStyleSheet(LIGHT)
        else:
            self.setStyleSheet(DARK)

    # def UpdateData(self):
    #     UpdateData = self.Alert()
    #     Btn = self.mainWindow.UpdateHome(UpdateData)
    #     return Btn
