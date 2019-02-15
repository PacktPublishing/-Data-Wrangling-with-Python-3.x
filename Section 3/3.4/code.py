from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

import csv

with open('hrdata.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es,reader,index = "my_index",doc_type = "my_type")
  