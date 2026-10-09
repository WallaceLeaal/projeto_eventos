from extensions import db

class Inscricao(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    participante_id = db.Column(db.Integer, db.ForeignKey("participante.id"), nullable=False)
    evento_id       = db.Column(db.Integer, db.ForeignKey("evento.id"), nullable=False)
    data_inscricao  = db.Column(db.String(10))
