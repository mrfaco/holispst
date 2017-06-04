from DataAccess.Entities.MateriaDTO import MateriaDTO
from Service.Entities.MateriaOutput import MateriaOutput

class Materia:
    def __init__(self,id,name,price,stock,date):
        self.Id = id
        self.Name=name
        self.Price=price
        self.Stock=stock
        self.FormatTime(date)

    def FormatTime(self,time):
        ts = time
        f = '%Y-%m-%d %H:%M:%S'
        formattedTime=ts.strftime(f)
        self.Date=formattedTime

    def ToMateriaDTO(self):
        return MateriaDTO(self.Id,self.Name,self.Price,self.Stock,self.Date)

    def __str__(self):
        return "Materia -- Id: {0}, Name: {1}, Price: {2}, Stock: {3}, Date: {4}".format(\
                self.Id,self.Name,self.Price,self.Stock,self.Date)

    def ToOutput(self):
        return MateriaOutput(self.Id,self.Name,self.Price,self.Stock,self.Price)