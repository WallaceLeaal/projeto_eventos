from extensions import db

class Evento(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    nome  = db.Column(db.String(120), nullable=False)
    data  = db.Column(db.String(10),  nullable=False)
    local = db.Column(db.String(120))
    vagas = db.Column(db.Integer)

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data": self.data,
            "local": self.local,
            "vagas": self.vagas
        }