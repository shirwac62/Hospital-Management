from web.extensions import db


class Department(db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(20),  nullable=False)
    Head_id = db.Column(db.Integer,  nullable=False)
    head_name = db.Column(db.String(30),  nullable=False)


