from typing import List

from elasticsearch import helpers

from app.db.elastic_db.connection import get_elastic_client
import os


DESCRIPTION_INDEX = os.environ['DESCRIPTION_INDEX']

def basic_search(txt: str) -> dict:
    try:
        query =  {
    "query": {
        "match": {
           "description": txt
        }
    }
}
        return get_elastic_client().search(index=DESCRIPTION_INDEX, body=query)
    except Exception as e:
        print(e)