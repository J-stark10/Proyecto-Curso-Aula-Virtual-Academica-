from datetime import datetime
from app.app import db

class Calificacion(db.Model):
    __tablename__ = "calificaciones"

    id = db.Column(db.Integer, primary_key=True)
    entrega_id = db.Column(db.Integer, db.ForeignKey("entregas.id"), nullable=False, unique=True)
    docente_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    retroalimentacion = db.Column(db.String(500))
    fecha_calificacion = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    entrega = db.relationship("Entrega", back_populates="calificacion")
    docente = db.relationship("Usuario", back_populates="calificaciones_realizadas")

    def __repr__(self):
        return f"<Calificacion entrega={self.entrega_id} nota={self.nota}>"
