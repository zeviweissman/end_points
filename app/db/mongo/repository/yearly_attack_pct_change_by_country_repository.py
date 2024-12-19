from typing import List
from app.db.mongo.connection import get_yearly_attack_pct_change_by_country_collection


def get_yearly_attack_pct_change_by_country(country: str) -> List[dict]:
    return list(get_yearly_attack_pct_change_by_country_collection().find({"country": country}).sort("year"))

