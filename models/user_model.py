from db.db import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String)
    phone_number = db.Column(db.String(50), nullable=True)
    
    def __init__(self, name, email, password, phone_number: str = None):
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
