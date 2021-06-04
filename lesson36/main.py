from elasticsearch import Elasticsearch
from datetime import datetime
from elasticsearch.helpers import streaming_bulk
# create connection
password = "i77GPf#%"
es = Elasticsearch(http_auth=('elastic', password))
# create index(table)
es.indices.create(index="some_index123", ignore=400)
# insert data
data = {
    "name": "41234123123",
    "timestamp": datetime.now(),
}
es.index(index="some_index123", body=data, )
