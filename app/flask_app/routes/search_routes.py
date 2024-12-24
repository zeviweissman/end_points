from flask import Blueprint, jsonify, render_template, request
from app.flask_app.service import search_service

search_blueprint = Blueprint('search_routes', __name__)

@search_blueprint.route('free_search/<text>')
def free_search(text: str):
    data = search_service.search_descriptions(text)
    return jsonify({"result": data}), 200