from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import health, countries, pong, fortune

    app.register_blueprint(health.bp)
    app.register_blueprint(countries.bp)
    app.register_blueprint(pong.bp)
    app.register_blueprint(fortune.bp)

    return app