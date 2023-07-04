from flask import Blueprint, jsonify, request
from flask_app.utils.countries_data import get_countries_data

countries_bp = Blueprint('countries', __name__)

@countries_bp.route('/countries', methods=['GET'])
def countries():
    continent = request.args.get('continent', None)
    population = request.args.get('population', None)
    countries = get_countries_data(continent, population)
    return jsonify({'status': 'success', 'data': countries})