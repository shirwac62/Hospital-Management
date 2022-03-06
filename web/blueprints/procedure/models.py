from web.extensions import db


class Procedure(db.Model):
    procedure_id = db.Column(db.Integer, primary_key=True)
    procedure_code = db.Column(db.Integer, unique=False, nullable=False)
    procedure_name = db.Column(db.String(20), unique=True, nullable=False)
    cost = db.Column(db.Integer, unique=False, nullable=False)
