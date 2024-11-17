from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime
import os

# Configuração do aplicativo
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Inicialização do banco de dados e JWT
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Modelos do banco de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)  # admin ou operador
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    dbo = db.Column(db.Float, nullable=False)
    dqo = db.Column(db.Float, nullable=False)
    ph = db.Column(db.Float, nullable=False)

# Rotas
@app.route('/register', methods=['POST'])
def register():
    """Cadastro de usuários."""
    data = request.json
    new_user = User(username=data['username'], password=data['password'], email=data['email'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "Usuário registrado"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Login de usuários."""
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity={'username': user.username, 'role': user.role, 'id': user.id})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Credenciais inválidas"}), 401

@app.route('/analyses', methods=['POST'])
@jwt_required()
def add_analysis():
    """Inserção de dados de análises."""
    current_user = get_jwt_identity()
    data = request.json
    new_analysis = Analysis(station_id=data['station_id'], user_id=current_user['id'], dbo=data['dbo'], dqo=data['dqo'], ph=data['ph'])
    db.session.add(new_analysis)
    db.session.commit()
    return jsonify({"msg": "Análise adicionada"}), 201

@app.route('/analyses/<int:station_id>', methods=['GET'])
@jwt_required()
def get_analyses(station_id):
    """Visualização de dados históricos de análises."""
    analyses = Analysis.query.filter_by(station_id=station_id).all()
    return jsonify([{'date': a.date, 'dbo': a.dbo, 'dqo': a.dqo, 'ph': a.ph} for a in analyses]), 200

@app.route('/login', methods=['GET'])
def login_page():
    """Página de login."""
    return render_template('login.html')

@app.route('/admin', methods=['GET'])
@jwt_required()
def admin_dashboard():
    """Dashboard do admin."""
    stations = Station.query.all()
    return render_template('dashboard_admin.html', stations=stations)

@app.route('/operator', methods=['GET'])
@jwt_required()
def operator_dashboard():
    """Dashboard do operador."""
    return render_template('dashboard_operator.html')

@app.route('/add_station', methods=['POST'])
@jwt_required()
def add_station():
    """Cadastro de novas estações."""
    data = request.json
    new_station = Station(name=data['name'], location=data['location'])
    db.session.add(new_station)
    db.session.commit()
    return jsonify({"msg": "Estação adicionada"}), 201

@app.route('/add_user', methods=['POST'])
@jwt_required()
def add_user():
    """Cadastro de novos usuários."""
    data = request.json
    new_user = User(username=data['username'], password=data['password'], email=data['email'], role=data['role'], station_id=data['station_id'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "Usuário adicionado"}), 201

if __name__ == '__main__':
    db.create_all()  # Cria as tabelas do banco de dados
    app.run(debug=True)
