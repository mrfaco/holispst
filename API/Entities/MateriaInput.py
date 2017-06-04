from Domain.Entities.Materia import Materia
import datetime

class MateriaInput:
    def __init__(self,name,price,stock):
        self.Name=name
        self.Price=price
        self.Stock=stock
    
    def __init__(self,fromDict):
        self.Name=fromDict['Name']
        self.Price=fromDict['Price']
        self.Stock=fromDict['Stock']

    def ToDomain(self):
        return Materia(0,self.Name,self.Price,self.Stock,datetime.datetime.now())
