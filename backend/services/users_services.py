from backend.models.users import User
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(data):
    user = User(
        username=data['username'],
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return user

def get_user(id):
    return User.query.get(id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def update_user(id, data):
    user = User.query.get(id)
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password_hash = generate_password_hash(data['password'])
    db.session.commit()
    return user

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user and check_password_hash(user.password_hash, password):
        return user
    return None