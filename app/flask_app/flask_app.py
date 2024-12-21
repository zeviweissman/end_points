from flask import Flask
from app.flask_app.routes import stats_blueprint
from app.flask_app.routes.relation_routes import relation_blueprint


def run_flask_app():
    app = Flask(__name__)
    app.register_blueprint(stats_blueprint, url_prefix='/stats')
    app.register_blueprint(relation_blueprint, url_prefix='/relation')
    app.run(debug=True)
