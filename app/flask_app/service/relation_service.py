import app.db.neo4j_db.repository.country_repository as country_repository
import app.db.neo4j_db.repository.group_reopsitory as group_repository
from app.folium_service.generate_maps import map_generator
from app.location_service.location_service import get_lat_lon



def get_map_for_groups_with_same_targets_by_country(country: str):
    data = group_repository.get_groups_with_same_targets_by_country(country)
    if data:
        location = get_lat_lon(country)
        map_generator(location=location, markers=[{"location": location, "popup": max(data, key=lambda di: len(di['groups'])), "tooltip": country}])
    else:
        raise Exception(f"No data for country {country}")


def get_map_for_countries_with_same_attack_types_by_group():
    data = country_repository.get_countries_with_same_attack_types_by_groups()
    popular_attacks = [{"location": get_lat_lon(attack['country']), "popup": {"attack type": attack['type'], "groups": attack['groups']}, "tooltip": attack['country']} for attack in data if len(attack['groups']) > 4]
    map_generator(location=popular_attacks[0]['location'], markers=popular_attacks)


def get_map_for_countries_with_unique_groups():
    data = country_repository.get_countries_with_unique_groups()
    countries = [{"location": get_lat_lon(country['country']), "popup": country['groups'], "tooltip": country['country']} for country in data]
    map_generator(location=countries[0]['location'], markers=countries)

def get_groups_with_same_targets():
    data = group_repository.get_groups_with_same_targets()
    if data:
        return [{"target": target["target"], "groups": target["groups"]} for target in data]

def get_map_for_groups_with_influence_info():
    data = group_repository.get_groups_with_influence_info()
    most_influential_group = max(data, key=lambda di: di['country_count'])
    locations = [{"location": get_lat_lon(country["name"]), "popup": {"areas": most_influential_group['country_count'], "targets": most_influential_group['target_count']}, "tooltip": most_influential_group["group"]} for country in most_influential_group['countries']]
    map_generator(location=locations[0]['location'], markers=locations)