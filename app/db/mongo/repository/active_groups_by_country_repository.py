from typing import List
from pymongo import DESCENDING
from app.db.mongo.connection import get_active_groups_by_country_collection


def get_active_groups_by_country_descending(country: str) -> List[dict]:
    return list(get_active_groups_by_country_collection().find({"country": country}).sort("value", DESCENDING))
