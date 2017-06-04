import json

class MateriaOutput:
    def __init__(self,id,name,price,stock,date):
        self.Id = id
        self.Name=name
        self.Price=price
        self.Stock=stock
        self.Date=date

    def ToJson(self):
        return json.dumps(self.__dict__)
