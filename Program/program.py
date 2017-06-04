import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from DataAccess.MateriasRepository import MateriasRepository
from Domain.MateriasDomainService import MateriasDomainService
import datetime
from Domain.Entities.Materia import Materia
from Service.MateriaService import MateriaService



repo = MateriasRepository()
domain = MateriasDomainService()
service = MateriaService()

if 1:
    for e in service.GetAllMaterias():
        print(e.ToJson())


if 0:
    mat = domain.GetMateriaById(7)
    print(mat)
    mat.Name="pelagato"
    domain.UpdateMateria(mat)
    print(service.GetMateriaById(7))

if 0:
    materias = domain.GetAllMaterias()
    for mat in materias:
        print(mat)



if 0:
    domain.SaveMateria(Materia(0,"peperoni",83,50,datetime.datetime.now()))

if 0:
    domain.DeleteMateriaById(51)

