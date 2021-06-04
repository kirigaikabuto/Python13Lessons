from elasticsearch import Elasticsearch

# create connection
password = "i77GPf#%"
es = Elasticsearch(http_auth=('elastic', password))
# get data from elastic
response = es.search(index="some_index123")
for i in response["hits"]["hits"]:
    print(i["_source"])
