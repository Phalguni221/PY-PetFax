from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ballpy(db.Model):
    __tablename__ = 'reptiles'
    id = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    fact = db.Column(db.Text)
