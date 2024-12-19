from typing import List

from pymongo import DESCENDING

from app.db.mongo.connection import get_total_damage_by_group_collection

def get_total_damage_by_group_descending(limit: int) -> List[dict]:
    return list(get_total_damage_by_group_collection().find({}).sort("value", DESCENDING).limit(limit))
