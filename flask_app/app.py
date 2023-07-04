```python
from flask import Flask
from flask_app.routes import health, countries, pong, fortune

def create_app():
    app = Flask(__name__)

    app.register_blueprint(health.bp)
    app.register_blueprint(countries.bp)
    app.register_blueprint(pong.bp)
    app.register_blueprint(fortune.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
```