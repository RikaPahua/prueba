from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,BLOB,ForeignKey,Float, Date
db=SQLAlchemy()

class Usuarios(db.model):
    __tablename__='Usuarios'
    idUsuario=Column(Integer,primary_key=True)
    nombre=Column(String,unique=True)
    sexo=Column(String)
    tipo=Column(String,nullable=False)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def eliminar(self,id):
        cat=self.consultaIndividuall(id)
        db.session.delete(cat)
        db.session.commit()

    def eliminacionLogica(self,id):
        tar = self.consultaIndividual(id)
        tar.estatus='Inactiva'
        tar.editar()

    def editar(self):
        db.session.merge(self)
        db.session.commit()
