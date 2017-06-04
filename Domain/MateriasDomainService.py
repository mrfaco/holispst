import datetime
from DataAccess.Entities.MateriaDTO import MateriaDTO
from .MateriasDomainServiceBase import MateriasDomainServiceBase
from DataAccess.MateriasRepository import MateriasRepository
from .Entities.Materia import Materia

class MateriasDomainService(MateriasDomainServiceBase):
    def __init__(self):
        self.MateriasRepository = MateriasRepository()
    
    def VerifyAll(self,Materia):
        self.errors=[]
        if Materia!=None:
            if not self.CheckIfIdIsInt(Materia.Id):
                self.errors.append("Id is invalid")
            if not self.CheckIfNameIsNotNull(Materia.Name):
                self.errors.append("Name is Invalid")
            if not self.CheckIfPriceIsCorrect(Materia.Price):
                self.errors.append("Price is invalid")
            if not self.CheckIfStockIsInt(Materia.Stock):
                self.errors.append("Stock is Invalid")
            if not self.CheckIfDateIsCorrect(Materia.Date):
                self.errors.append("Date is invalid")
    
    def CheckIfIdIsInt(self,Id):
        return isinstance(Id,int) 
    def CheckIfNameIsNotNull(self,name):
        return (isinstance(name,str) and name!="")
    def CheckIfPriceIsCorrect(self,price):
        return (isinstance(price,float) and price>=0)
    def CheckIfStockIsInt(self,stock):
        return (isinstance(stock,int) and stock>=0)
    def CheckIfDateIsCorrect(self,date):
        return True
    
    def GetMateriaById(self,Id):
        materia = self.MateriasRepository.GetMateriaById(Id)
        if len(materia)>0:
            materia=materia[0]
            return Materia(materia[0],materia[1],materia[2],materia[3],materia[4])
        else:
            print("materia with Id={0} doesn't exist in database".format(Id))
    
    def SaveMateria(self,Materia):
        self.VerifyAll(Materia)
        if self.errors==[]:
            self.MateriasRepository.SaveMateria(Materia.ToMateriaDTO())
        else:
            for e in self.errors:
                print(e)
    
    def GetAllMaterias(self):
        returns = []
        materias = self.MateriasRepository.GetAllMaterias()
        for mat in materias:
            returns.append(Materia(mat[0],mat[1],mat[2],mat[3],mat[4]))
        return returns

    def DeleteMateriaById(self,Id):
        if len(self.MateriasRepository.GetMateriaById(Id))>0:
            self.MateriasRepository.DeleteMateriaById(Id)
        else:
            print("Materia with Id={0} doesn't exist in database".format(Id))
        
    def UpdateMateria(self,Materia):
        Materia.FormatTime(datetime.datetime.now())
        if len(self.MateriasRepository.GetMateriaById(Materia.Id))>0:
            self.VerifyAll(Materia)
            if self.errors==[]:
                self.MateriasRepository.UpdateMateria(Materia.ToMateriaDTO())
            else:
                raise Exception(self.errors.__str__())
        else:
            raise Exception("Materia with Id={0} doesn't exist in database".format(Materia.Id))
