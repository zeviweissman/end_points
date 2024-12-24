from toolz import pipe

from app.db.elastic_db.model import DescriptionModel
from app.db.elastic_db.repository import description_repository
from app.db.postgres.data_models import TerrorAttackModel
from app.db.postgres.repository import terror_attack_repository
from app.db.postgres.sql_alchemy_models import TerrorAttack
from app.utils import convert_utils
from typing import List


def get_terror_attack_by_id(terror_attack_id: int) -> TerrorAttack:
    return terror_attack_repository.get_terror_attack_by_id(terror_attack_id).value_or(None)


def parse_desc_and_terror_attack_to_terror_attack_model(description: DescriptionModel) -> TerrorAttackModel:
    return convert_utils.parse_desc_and_terror_attack_to_terror_attack_model(description.description, get_terror_attack_by_id(description.terror_attack_id))


def get_list_of_terror_attacks_from_description(descriptions: List[DescriptionModel]) -> list[TerrorAttackModel]:
    return [parse_desc_and_terror_attack_to_terror_attack_model(description) for description in descriptions]


def search_descriptions(txt: str):
    return pipe(
        description_repository.basic_search(txt)['hits']['hits'],
        convert_utils.elastic_hits_to_description_model,
        get_list_of_terror_attacks_from_description,
        convert_utils.pydantic_models_as_dictionary
    )

