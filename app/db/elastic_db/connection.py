from elasticsearch import Elasticsearch
import os




DESCRIPTION_INDEX = os.environ['DESCRIPTION_INDEX']


def get_elastic_client():
    return Elasticsearch(
        ['http://localhost:9200']
    )



