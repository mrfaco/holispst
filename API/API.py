import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Service.MateriaService import MateriaService
from Entities.MateriaInput import MateriaInput
import json


materiaService = MateriaService()

from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/Materias/')
def GetAllMaterias():
     output = []
     for item in materiaService.GetAllMaterias():
         output.append(item.__dict__)
     return jsonify(output)

@app.route('/Materias/<id>')
def GetMateriaById(id):
     item = materiaService.GetMateriaById(id)
     return jsonify(item.__dict__)

@app.route('/Materias/',methods=['POST'])
def SaveMateria():
    datos = json.loads(request.data)
    materiaInput=MateriaInput(datos)
    print(materiaInput.Name)
    materiaService.SaveMateria(materiaInput)
    return jsonify("ok")


if __name__=="__main__":
    app.run()