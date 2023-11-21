import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# User model

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    phone_number = db.Column(db.String(50), nullable=True)
    
    def __init__(self, id, name, email, password, phone_number: str = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        

# Init db
def init_db():
    DB_Name =  "sample.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_Name
    db.init_app(app)

# Users crud

# Create user
@app.route('/create_user', methods=['POST'])
def create():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone_number = request.form.get('phone_number', None)
    
    user = User(id, name, email, password, phone_number)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully!'})

# Get all users
@app.route('/users', methods=['GET'])
def get_all():
    # Query params: limit, offset
    limit = request.args.get('limit', 10)
    offset = request.args.get('offset', 0)
    
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
        
    return jsonify({'users': output})

# Get single user
@app.route('/user/<id>', methods=['GET'])
def get_one(id):
    user = User.query.filter_by(id=id).first()
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['phone_number'] = user.phone_number
    
    return jsonify({'user': user_data})

# Patch user
@app.route('/user/<id>', methods=['PATCH'])
def patch(id):
    user = User.query.filter_by(id=id).first()
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    user.name = request.json.get('name', user.name)
    user.email = request.json.get('email', user.email)
    user.password = request.json.get('password', user.password)
    user.phone_number = request.json.get('phone_number', user.phone_number)
    
    db.session.commit()
    
    return jsonify({'message': 'User updated successfully!'})

# Delete user
@app.route('/user/<id>', methods=['DELETE'])
def delete(id):
    user = User.query.filter_by(id=id).first()
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully!'})

# Home page
@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

# Init db
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    