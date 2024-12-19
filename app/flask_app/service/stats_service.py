from typing import List

import app.db.mongo.repository.yearly_attack_pct_change_by_country_repository as yearly_attack_pct_change_repos
import app.folium_service.generate_maps as map_generator
import app.db.mongo.repository.active_groups_by_country_repository as active_groups_by_country_repos
import app.db.mongo.repository.avg_damage_by_country_repository as avg_damage_by_country_repos
import app.db.mongo.repository.total_damage_by_attack_type_repository as total_damage_by_attack_repos
import app.db.mongo.repository.total_damage_by_group_repository as total_damage_by_group_repos

def get_map_for_yearly_attack_pct_change_by_country(country: str):
    data = yearly_attack_pct_change_repos.get_yearly_attack_pct_change_by_country(country)
    if data:
        parsed_data = [{"year": d['year'], "percent_change":d['value']} for d in data]
        map_generator.generate_map_for_yearly_attack_pct_change_by_country(country, parsed_data)
    else:
        raise Exception(f"No data for country {country}")

def get_map_for_most_active_groups_by_country(country: str):
    data = active_groups_by_country_repos.get_active_groups_by_country_descending(country)
    if data:
        parsed_data = [{"group": d['group'], "attacks_count": d['value']} for d in data]
        map_generator.generate_map_for_yearly_attack_pct_change_by_country(country, parsed_data)
    else:
        raise Exception(f"No data for country {country}")


def get_map_for_avg_damage_by_country(country: str):
    data = avg_damage_by_country_repos.get_avg_damage_by_country(country)
    if data:
        map_generator.generate_map_for_avg_damage_by_country(country, data['value'])
    else:
        raise Exception(f"No data for country {country}")


def get_total_damage_by_attack_type_descending(limit: int) -> List[dict]:
    data = total_damage_by_attack_repos.get_total_damage_by_attack_type_descending(limit)
    return [{"type": d['type'], "value": d['value']} for d in data]

def get_total_damage_by_group_descending(limit: int) -> List[dict]:
    data = total_damage_by_group_repos.get_total_damage_by_group_descending(limit)
    return [{"group": d['group'], "value": d['value']} for d in data]