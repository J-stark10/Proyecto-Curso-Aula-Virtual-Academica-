from datetime import datetime
from app.app import db


class Entrega(db.Model):
    __tablename__ = "entregas"
    __table_args__ = (
        db.UniqueConstraint("tarea_id", "estudiante_id", name="uq_tarea_estudiante"),
    )

    id = db.Column(db.Integer, primary_key=True)
    tarea_id = db.Column(db.Integer, db.ForeignKey("tareas.id"), nullable=False)
    estudiante_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    archivo = db.Column(db.String(255), nullable=False)  # ruta relativa en uploads/entregas/
    comentario = db.Column(db.String(255))
    fecha_entrega = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # Solo dos estados persistidos: "entregado" o "revisado".
    # "pendiente" (sin entregar) se calcula dinámicamente comparando
    # las inscripciones del curso contra las entregas existentes — no se guarda en BD.
    estado = db.Column(db.String(20), nullable=False, default="entregado")

    tarea = db.relationship("Tarea", back_populates="entregas")
    estudiante = db.relationship("Usuario", back_populates="entregas")
    calificacion = db.relationship("Calificacion", back_populates="entrega", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Entrega tarea={self.tarea_id} estudiante={self.estudiante_id} [{self.estado}]>"
