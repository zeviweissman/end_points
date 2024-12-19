from typing import List

import folium
from pathlib import Path

from app.location_service.location_service import get_lat_lon

PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATE_PATH = PROJECT_ROOT/ 'app' / 'flask_app' / 'templates'


def generate_map_for_yearly_attack_pct_change_by_country(country: str, yearly_info: List[dict]):
    folium_map = folium.Map(location=get_lat_lon(country), zoom_start=3)
    folium.Marker(location=get_lat_lon(country),
                  popup=f'<h1>{yearly_info}<h1>',
                  tooltip=country,
                  icon=folium.Icon(icon='pushpin', color='red')).add_to(folium_map)
    folium_map.save(f'{TEMPLATE_PATH}\map.html')


def generate_map_for_most_active_groups_by_country(country: str, most_active_group: dict):
    folium_map = folium.Map(location=get_lat_lon(country), zoom_start=3)
    folium.Marker(location=get_lat_lon(country),
                  popup=f'<h1>{most_active_group}<h1>',
                  tooltip=country,
                  icon=folium.Icon(icon='pushpin', color='red')).add_to(folium_map)
    folium_map.save(f'{TEMPLATE_PATH}\map.html')


def generate_map_for_avg_damage_by_country(country: str, avg_damage: int):
    folium_map = folium.Map(location=get_lat_lon(country), zoom_start=3)
    folium.Marker(location=get_lat_lon(country),
                  popup=f'<h1>average damage: {avg_damage}<h1>',
                  tooltip=country,
                  icon=folium.Icon(icon='pushpin', color='red')
                  ).add_to(folium_map)
    folium_map.save(f'{TEMPLATE_PATH}\map.html')
