from extensions import db
from models.evento import Evento

class EventoDAO:

    @staticmethod
    def salvar(evento):
        db.session.add(evento)
        db.session.commit()

    @staticmethod
    def listar():
        return Evento.query.all()

    @staticmethod
    def buscar_por_id(id_evento):
        return Evento.query.get(id_evento)

    @staticmethod
    def atualizar():
        db.session.commit()

    @staticmethod
    def remover(evento):
        db.session.delete(evento)
        db.session.commit()
