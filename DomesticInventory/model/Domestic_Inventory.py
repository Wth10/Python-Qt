class Domestic_Inventory:
    def __init__(self, Id, Name, Room, Description, Brand, Date, Price, Serie) -> None:
        self.Id = Id
        self.Name = Name
        self.Room = Room
        self.Description = Description
        self.Brand = Brand
        self.Date = Date
        self.Price = Price
        self.Serie = Serie


class EditDomestic_Inventory:
    def __init__(self, Name, Room, Description, Brand, Date, Price, Serie) -> None:
        self.Name = Name
        self.Room = Room
        self.Description = Description
        self.Brand = Brand
        self.Date = Date
        self.Price = Price
        self.Serie = Serie
