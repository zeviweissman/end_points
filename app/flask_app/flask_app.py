from flask import Flask
from app.flask_app.routes import stats_blueprint


def run_flask_app():
    app = Flask(__name__)
    app.register_blueprint(stats_blueprint, url_prefix='/stats')
    app.run(debug=True)