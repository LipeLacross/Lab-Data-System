from flask import Blueprint, request, jsonify
from models import User, db
from werkzeug.security import generate_password_hash

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], password=hashed_password, email=data['email'], role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201
