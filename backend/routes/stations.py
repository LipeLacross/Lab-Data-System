from flask import Blueprint, request, jsonify
from models import Station, db

bp = Blueprint('stations', __name__, url_prefix='/stations')

@bp.route('/', methods=['GET'])
def get_stations():
    stations = Station.query.all()
    return jsonify([{"id": station.id, "name": station.name} for station in stations])

@bp.route('/', methods=['POST'])
def create_station():
    data = request.get_json()
    station = Station(name=data['name'], location=data['location'])
    db.session.add(station)
    db.session.commit()
    return jsonify({"msg": "Station created"}), 201
