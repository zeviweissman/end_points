from flask import Blueprint, jsonify, render_template, request
import app.flask_app.service.relation_service as relation_service

relation_blueprint = Blueprint('relation_routes', __name__)

@relation_blueprint.route('/')
def get_map_for():

    return render_template('map.html')