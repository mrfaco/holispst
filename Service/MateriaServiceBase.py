from abc import ABC,abstractmethod

class MateriaServiceBase:
    @abstractmethod
    def GetAllMaterias(self):
        pass
    @abstractmethod
    def GetMateriaById(self,id):
        pass
    @abstractmethod
    def SaveMateria(self,materia):
        pass
    @abstractmethod
    def UpdateMateria(self,materia,id):
        pass