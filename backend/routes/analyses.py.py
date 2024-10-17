from flask import Blueprint, request, jsonify
from models import Analysis, db

bp = Blueprint('analyses', __name__, url_prefix='/analyses')

@bp.route('/', methods=['POST'])
def add_analysis():
    data = request.get_json()
    analysis = Analysis(station_id=data['station_id'], user_id=data['user_id'], dbo=data['dbo'], dqo=data['dqo'], ph=data['ph'])
    db.session.add(analysis)
    db.session.commit()
    return jsonify({"msg": "Analysis data added"}), 201
