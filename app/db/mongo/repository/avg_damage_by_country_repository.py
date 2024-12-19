from app.db.mongo.connection import get_avg_damage_by_country_collection


def get_avg_damage_by_country(country: str):
    return get_avg_damage_by_country_collection().find_one({"country": country})
