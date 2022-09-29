class Covid19Brazil:
    def __init__(
        self, uid, uf, state, cases, deaths, suspects, refuses, datetime
    ) -> None:
        self.uid = uid
        self.uf = uf
        self.state = state
        self.cases = cases
        self.deaths = deaths
        self.suspects = suspects
        self.refuses = refuses
        self.datetime = datetime

    def __str__(self):
        return f"ID = {self.uid}\n UF = {self.uf}\n Cidade = {self.state}"
