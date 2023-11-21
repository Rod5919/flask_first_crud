from models.user_model import User
from db.db import db

from utils.encryptor import Encryptor

def get_all_users(limit: int = None, offset: int = None):
    users = User.query.limit(limit).offset(offset).all()
    
    output = []
    
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['password'] = user.password
        user_data['phone_number'] = user.phone_number
        output.append(user_data)
        
    return users

def get_one_user(id: int):
    user = User.query.filter_by(id=id).first()
    
    if not user:
        return None
    
    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['phone_number'] = user.phone_number
    
    return user_data

def create_user(name: str, email: str, password: str, phone_number: str = None):
    password = Encryptor.encrypt(password)
    user = User(name, email, password, phone_number)
    db.session.add(user)
    db.session.commit()
    
    return user

def patch_user(id: int, name: str = None, email: str = None, password: str = None, phone_number: str = None):
    user = User.query.filter_by(id=id).first()
    
    if not user:
        return None
    
    user.name = name if name else user.name
    user.email = email if email else user.email
    user.password = password if password else user.password
    user.phone_number = phone_number if phone_number else user.phone_number
    
    db.session.commit()
    
    return user

def delete_user(id: int):
    user = User.query.filter_by(id=id).first()
    
    if not user:
        return None
    
    db.session.delete(user)
    db.session.commit()
    
    return user