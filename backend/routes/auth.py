from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Invalid credentials"}), 401
