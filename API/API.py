import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Service.MateriaService import MateriaService
from Entities.MateriaInput import MateriaInput
import json
from flask_cors import CORS

materiaService = MateriaService()

from flask import Flask,jsonify,request
app = Flask(__name__)
CORS(app)

@app.route('/Materias/')
def GetAllMaterias():
     output = []
     for item in materiaService.GetAllMaterias():
         output.append(item.__dict__)
     return jsonify(output)

@app.route('/Materias/<id>')
def GetMateriaById(id):
     item = materiaService.GetMateriaById(id)
     print(item)
     return jsonify(item.__dict__)

@app.route('/Materias/',methods=['POST'])
def SaveMateria():
    datos = json.loads(request.data)
    materiaInput=MateriaInput(datos)
    print(materiaInput)
    try:
        materiaService.SaveMateria(materiaInput)
        return jsonify("Materia created")
    except Exception as e:
        return jsonify(e.args[0].__str__()),400
        
@app.route("/Materias/<id>",methods=['PUT'])
def UpdateMateria(id):
    datos=json.loads(request.data)
    materiaInput=MateriaInput(datos)
    print(materiaInput)
    try:
        materiaService.UpdateMateria(materiaInput,id)
        return jsonify("Edited correctly")
    except Exception as e:
        return jsonify(e.args[0].__str__()),400
        
    
if __name__=="__main__":
    app.run()
