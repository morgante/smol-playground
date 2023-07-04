from flask import jsonify
from flask_app import app
from flask_app.utils.health_check import health_check

@app.route('/health')
def health():
    health_status = health_check()
    return jsonify(health_status)