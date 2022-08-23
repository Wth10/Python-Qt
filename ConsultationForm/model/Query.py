class Query:
    def __init__(self, Id, Name, Email, Telephone, Date, Status, Description) -> None:
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.Telephone = Telephone
        self.Date = Date
        self.Status = Status
        self.Description = Description


class EditQuery:
    def __init__(self, Name, Email, Telephone, Date, Status, Description) -> None:
        self.Name = Name
        self.Email = Email
        self.Telephone = Telephone
        self.Date = Date
        self.Status = Status
        self.Description = Description
