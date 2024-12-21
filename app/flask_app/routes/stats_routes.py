from flask import Blueprint, jsonify, render_template, request
import app.flask_app.service.stats_service as stats_service

stats_blueprint = Blueprint('stats_routes', __name__)

@stats_blueprint.route('/yearly/<country>')
def get_map_for_yearly_attack_pct_change_by_country(country):
    stats_service.get_map_for_yearly_attack_pct_change_by_country(country)
    return render_template('map.html')


@stats_blueprint.route('/active/<country>')
def get_map_for_most_active_groups_by_country(country):
    stats_service.get_map_for_most_active_groups_by_country(country)
    return render_template('map.html')


@stats_blueprint.route('/average/<country>')
def get_map_for_avg_damage_by_country(country):
    stats_service.get_map_for_avg_damage_by_country(country)
    return render_template('map.html')


@stats_blueprint.route('/damage_by_type')
def get_total_damage_by_attack_type():
    limit = request.args.get('limit') or 5
    data = stats_service.get_total_damage_by_attack_type_descending(int(limit))
    return jsonify(data), 200

@stats_blueprint.route('/damage_by_group')
def get_total_damage_by_group():
    limit = request.args.get('limit') or 5
    data = stats_service.get_total_damage_by_group_descending(int(limit))
    return jsonify(data), 200
