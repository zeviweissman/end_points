from typing import List

from app.db.neo4j_db.crud import data_query

def get_countries_with_same_attack_types_by_groups() -> List[dict]:
    query = """ 
            match  (g:Group) -[rel:ATTACKED]- (c:Country)
            return rel.type as type, collect(DISTINCT g.name) as groups, c.name as country
            """
    return data_query(query=query)

def get_countries_with_unique_groups() -> List[dict]:
    query = """
             match  (g:Group) -[rel:ATTACKED]- (c:Country)
            return  count(DISTINCT g.name) as group_count, collect(DISTINCT g.name) as groups, c.name as country
            """
    return data_query(query=query)

