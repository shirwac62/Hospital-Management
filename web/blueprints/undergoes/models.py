from web.extensions import db


class Undergoes(db.Model):
    undergoes_id = db.Column(db.Integer, primary_key=True)
    doc_full_name = db.Column(db.String(20),nullable=False)
    pat_full_name = db.Column(db.String(20), nullable=False)
    procedure_code = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    room_no = db.Column(db.Integer,  nullable=False)

