from web.extensions import db


class department(db.Model):
    department_id = db.Column(db.string, primary_key=True)
    department_name = db.Column(db.String(20), unique=True, nullable=False)
    Head_id = db.Column(db.integer(20), unique=True, nullable=False)
    First_name = db.Column(db.String(20), unique=True, nullable=False)
    Last_name = db.Column(db.String(20), unique=True, nullable=False)
