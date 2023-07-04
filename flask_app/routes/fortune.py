from flask import Blueprint, jsonify
from flask_app.utils.fortune_generator import fortune_generator

fortune = Blueprint('fortune', __name__)

@fortune.route('/fortune', methods=['GET'])
def get_fortune():
    fortune_cookie = fortune_generator()
    return jsonify({'fortune': fortune_cookie})