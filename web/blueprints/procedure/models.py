from web.extensions import db


class Procedure(db.Model):
    procedure_id = db.Column(db.Integer, primary_key=True)
    procedure_code = db.Column(db.Integer, unique=True,nullable=False)
    procedure_name = db.Column(db.String(20),  nullable=False)
    cost = db.Column(db.Integer(20), unique=True, nullable=False)


