from Domain.Entities.Materia import Materia
from .MateriaServiceBase import MateriaServiceBase
from Domain.MateriasDomainService import MateriasDomainService
from .Entities.MateriaOutput import MateriaOutput
#from API.Entities.MateriaOutput import MateriaOutput
class MateriaService(MateriaServiceBase):
    def __init__(self):
        self.materiasDomainService = MateriasDomainService()
    def GetAllMaterias(self):
        returns = []
        for mat in self.materiasDomainService.GetAllMaterias():
            returns.append(mat.ToOutput())
        return returns
    
    def GetMateriaById(self,Id):
        mat = self.materiasDomainService.GetMateriaById(Id)
        return mat.ToOutput

    def SaveMateria(self,materiaInput):
        self.materiasDomainService.SaveMateria(materiaInput.ToDomain())

    
