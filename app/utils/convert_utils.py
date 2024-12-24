from typing import List

from pydantic import BaseModel

from app.db.elastic_db.model import DescriptionModel
from app.db.postgres.data_models import *
from app.db.postgres.sql_alchemy_models import TerrorAttack
import toolz as t


def parse_desc_and_terror_attack_to_terror_attack_model(description: str, terror_attack: TerrorAttack) -> TerrorAttackModel:
    return TerrorAttackModel(
        city=CityModel(
            name=terror_attack.city.name,
            country=CountryModel(
                name=terror_attack.city.country.name,
            )
        ),
        attack_type=AttackTypeModel(
            type=terror_attack.attack_type.name
        ),
        description=[description],
        total_wounded=terror_attack.total_wounded,
        total_killed=terror_attack.total_killed,
        date=terror_attack.date,
        id=terror_attack.id,
        group=GroupModel(
            name=terror_attack.group.name,
        )
    )


def elastic_hit_to_description_model(hit: dict) -> DescriptionModel:
    return DescriptionModel(
        description=t.get_in(['_source', 'description'], hit),
        terror_attack_id=t.get_in(['_source', 'terror_attack_id'], hit)
    )

def elastic_hits_to_description_model(hits: List[dict]) -> List[DescriptionModel]:
    return [elastic_hit_to_description_model(hit) for hit in hits]


def pydantic_models_as_dictionary(models: List[BaseModel]) -> List[dict]:
    return [model.model_dump() for model in models]
