from abc import ABC, abstractmethod

class MateriasRepositoryBase(ABC):
    @abstractmethod
    def GetMateriaById(self,Id):
        pass
    @abstractmethod
    def SaveMateria(self,MateriaDTO):
        pass    
    @abstractmethod
    def GetAllMaterias(self):
        pass
    @abstractmethod
    def DeleteMateriaById(self):
        pass
    @abstractmethod
    def UpdateMateria(self,Id):
        pass