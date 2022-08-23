from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from decimal import Decimal
import locale

File_Qt = "MainQt.ui"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.ButtonSubmit.clicked.connect(self.Calcule)

    def FormatNumber(self, Value):
        locale.setlocale(locale.LC_ALL, "pt_BR")
        valor = Decimal(Value)
        FormatNumber = locale.currency(valor, grouping=True)
        return FormatNumber

    def Calcule(self):
        InputNome = str(self.InputNome.text())
        InputHora = str(self.InputHora.text())
        InputDia = str(self.InputDia.text())
        InputSalario = str(self.InputSalario.text())

        # Alertas
        AlertNome = self.AlertNome.text()
        AlertDia = self.AlertDia.text()
        AlertSemana = self.AlertSemana.text()
        AlertTotal = self.AlertTotal.text()

        # Alertas Resultado
        SalarioHora = str(self.SalarioHora.text())
        SalarioDia = str(self.SalarioDia.text())
        SalarioSemanal = str(self.SalarioSemanal.text())
        SalarioMensal = str(self.SalarioMensal.text())
        SalarioAnual = str(self.SalarioAnual.text())

        if InputNome == "" or InputHora == "" or InputDia == "" or InputSalario == "":
            self.AlertErro.setText("Preencha Todos Os Campos")

        else:
            # Limpar Alert De Erro
            self.AlertErro.clear()

            # Mostrar Valor Das Inputs
            self.AlertNome.setText(f"Seu Nome: {InputNome}")
            self.AlertDia.setText(str(f"Horas De Trabalho Por Dia: {InputHora}"))
            self.AlertSemana.setText(str(f"Dias De Trabalho Por Semana: {InputDia}"))
            self.AlertTotal.setText(str(self.FormatNumber(InputSalario)))

            # Salario Mensal
            MonthlySalaryResult = int(InputSalario) / 12
            FormatMensal = self.FormatNumber(MonthlySalaryResult)
            self.SalarioMensal.setText(f"Salário Por Hora: {FormatMensal}")

            # Salario Samanal
            WeeklySalaryResult = MonthlySalaryResult / 4.35
            FormatSemanal = self.FormatNumber(WeeklySalaryResult)
            self.SalarioSemanal.setText(f"Salário Semanal: {FormatSemanal}")

            # Salario Diário
            SalaryResultPerDay = WeeklySalaryResult / int(InputDia)
            FormatDia = self.FormatNumber(SalaryResultPerDay)
            self.SalarioDia.setText(f"Salário Diário: {FormatDia}")

            # Salario Por Hora
            EarningsPerHour = SalaryResultPerDay / int(InputHora)
            FormatHora = self.FormatNumber(EarningsPerHour)
            self.SalarioHora.setText(f"Salário Por Hora: {FormatHora}")

            # Salario Anual
            FormatTotal = self.FormatNumber(InputSalario)
            self.SalarioAnual.setText(f"Salário Anual: {FormatTotal}")

            # Limpar Input
            self.InputNome.clear()
            self.InputHora.clear()
            self.InputDia.clear()
            self.InputSalario.clear()
