from flask import jsonify
from flask_app import app

@app.route('/pong')
def pong():
    return jsonify({
        'message': 'Hello'
    })