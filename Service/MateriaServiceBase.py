from abc import ABC,abstractmethod

class MateriaServiceBase:
    @abstractmethod
    def GetAllMaterias(self):
        pass
    def GetMateriaById(self,id):
        pass