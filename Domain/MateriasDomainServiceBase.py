from abc import ABC,abstractmethod

class MateriasDomainServiceBase(ABC):
    @abstractmethod
    def VerifyAll(self,Materia):
        pass
    @abstractmethod
    def GetMateriaById(self,Id):
        pass
    @abstractmethod
    def SaveMateria(self,Materia):
        pass
    def GetAllMaterias(self):
        pass
    def UpdateMateriaById(self,Materia):
        pass