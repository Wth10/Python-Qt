class Revenue:
    def __init__(self, Id, Description, Price) -> None:
        self.Id = Id
        self.Description = Description
        self.Price = Price


class EditRevenue:
    def __init__(self, Description, Price) -> None:
        self.Description = Description
        self.Price = Price
