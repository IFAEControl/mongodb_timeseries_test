from datetime import datetime, timezone
from pymongo import MongoClient

# Type of doc
base_doc_cluster = {
  'timestamp': datetime.now(tz=timezone.utc),
  'metric_name': 'lst1.camera.clusters.humidity',
  'values': {
    cluster: {
      minute: {
        second: None for second in range(60)
      } for minute in range(60)
    } for cluster in range(7)
  }
}
base_doc_pixel = {
  'timestamp': datetime.now(tz=timezone.utc),
  'metric_name': 'lst1.camera.clusters.pixels.scbtemp',
  'values': {
    cluster: {
      pixel: {
        minute: {
          second: None for second in range(60)
        } for minute in range(60)
      } for pixel in range(7)
    } for cluster in range(7)
  }
}

base_doc_single = {
  'timestamp': datetime.now(tz=timezone.utc),
  'metric_name': 'lst1.camera.ecc.humidity',
  'values': {
    minute: {
      second: None for second in range(60)
    } for minute in range(60)
  }
}


class Filler(object):
  def __init__(self, db_name, host='localhost', port=27017):
    self._client = MongoClient(host, port)
    self._db = self._client[db_name]

  def drop_collection(self, collection):
    col = self._db[collection]
    col.drop()
