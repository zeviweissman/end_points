from typing import List

from app.db.neo4j_db.crud import data_query

def get_groups_with_same_targets_by_country(country: str) -> List[dict]:
    query = """ 
            match  (g:Group) -[rel:ATTACKED]- (c:Country{name:$country})
            return rel.target as target, collect(DISTINCT g.name) as groups, c.name as country
            """
    return data_query(query=query, params={'country': country})

def get_groups_with_same_targets() -> List[dict]:
    query = """
            match  (g:Group) -[rel:ATTACKED]- (c:Country)
            return rel.target as target, collect(g.name) as groups, count(g.name) as count
            """
    return data_query(query=query)

def get_groups_with_influence_info() -> List[dict]:
    query = """
            match  (g:Group) -[rel:ATTACKED]- (c:Country)
            return  g.name as group, count(DISTINCT c) as country_count, count(DISTINCT rel.target) as target_count, count(DISTINCT rel.type) as type_count
            """
    return data_query(query=query)

