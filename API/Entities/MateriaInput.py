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

    def ToDomainForNew(self):
        return Materia(0,self.Name,self.Price,self.Stock,datetime.datetime.now())
    
    def ToDomainForUpdate(self,id):
        return Materia(int(id),self.Name,self.Price,self.Stock,datetime.datetime.now())

    def __str__(self):

        return "Name: {0}, Price: {1}, Stock: {2}".format(\
                self.Name,self.Price,self.Stock)