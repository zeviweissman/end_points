from flask import Flask
from app.flask_app.routes import stats_blueprint, search_blueprint, relation_blueprint


def run_flask_app():
    app = Flask(__name__)
    app.register_blueprint(stats_blueprint, url_prefix='/stats')
    app.register_blueprint(relation_blueprint, url_prefix='/relation')
    app.register_blueprint(search_blueprint, url_prefix='/search')
    app.run(debug=True)
