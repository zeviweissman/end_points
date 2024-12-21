from flask import Blueprint, jsonify, render_template, request
import app.flask_app.service.relation_service as relation_service

relation_blueprint = Blueprint('relation_routes', __name__)

@relation_blueprint.route('same_targets/<country>')
def get_map_for_groups_with_same_targets_by_country(country: str):
    relation_service.get_map_for_groups_with_same_targets_by_country(country)
    return render_template('map.html')


@relation_blueprint.route('same_attacks/')
def get_map_for_countries_with_same_attack_types_by_group():
    relation_service.get_map_for_countries_with_same_attack_types_by_group()
    return render_template("map.html")

@relation_blueprint.route('unique_groups/')
def get_map_for_countries_with_unique_groups():
    relation_service.get_map_for_countries_with_unique_groups()
    return render_template("map.html")

@relation_blueprint.route('same_targets/')
def get_groups_with_same_targets():
    data = relation_service.get_groups_with_same_targets()
    return jsonify(data), 200

@relation_blueprint.route('influence_info/')
def get_map_for_groups_with_influence_info():
    relation_service.get_map_for_groups_with_influence_info()
    return render_template("map.html")