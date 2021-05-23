from wtforms.validators import Email
from swbpacote import db

class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class ContactModel(BaseModel):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telefone = db.Column(db.Integer, nullable=False)


class ClienteModel(BaseModel):
    __tablename__ = 'cliente'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)



class LivroModel(BaseModel):
    __tablename__ = 'livro'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer)