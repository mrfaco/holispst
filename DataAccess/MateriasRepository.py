from .MateriasRepositoryBase import MateriasRepositoryBase
import MySQLdb

class MateriasRepository(MateriasRepositoryBase):
    def __init__(self):
        self.DBUser = "root"
        self.DBPass = "lalalala"
        self.DBUrl = "localhost"
        self.DBName = "holispst"

    def StartConnection(self):
        self.Connection = MySQLdb.Connect(
                    host=self.DBUrl,
                     user=self.DBUser,         
                     passwd=self.DBPass,
                     db=self.DBName,
                     )
        
    def GetMateriaById(self,Id):
        self.StartConnection()
        cursor = self.Connection.cursor()
        cursor.execute("SELECT * FROM MATERIAS WHERE id={0};".format(Id))
        returns = cursor.fetchall()
        self.Connection.close()
        return returns
    
    def SaveMateria(self, MateriaDTO):
        self.StartConnection()
        cursor = self.Connection.cursor()
        sql="INSERT INTO MATERIAS(name,price,stock,datemodified) values('{0}',{1},{2},'{3}');"\
            .format(MateriaDTO.Name,MateriaDTO.Price,MateriaDTO.Stock,MateriaDTO.Date)
        print(sql)
        cursor.execute(sql)
        self.Connection.commit()
        self.Connection.close()

    def GetAllMaterias(self):
        self.StartConnection()
        cursor = self.Connection.cursor()
        cursor.execute("SELECT * FROM MATERIAS;")
        returns=cursor.fetchall()
        self.Connection.close()
        return returns
    
    def DeleteMateriaById(self,Id):
        self.StartConnection()
        cursor=self.Connection.cursor()
        cursor.execute("DELETE FROM MATERIAS WHERE id = {0}".format(Id))
        self.Connection.commit()
        self.Connection.close()

    def UpdateMateria(self,MateriaDTO):
        self.StartConnection()
        cursor=self.Connection.cursor()
        cursor.execute("UPDATE MATERIAS set name='{0}',price={1},stock={2},datemodified='{3}' WHERE id = {4}".format\
                      (MateriaDTO.Name,MateriaDTO.Price,MateriaDTO.Stock,MateriaDTO.Date,MateriaDTO.Id))
        self.Connection.commit()
        self.Connection.close()

