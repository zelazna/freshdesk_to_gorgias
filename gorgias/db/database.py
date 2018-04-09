import json


class Database:
    """The Database use a simple json as a datasource"""

    def __init__(self, datasource):
        self._datasource = datasource

    def find(self, data_type, id):
        with open(self._datasource) as f:
            read_data = json.loads(f.read())
            return id in read_data[data_type]
        f.closed

    def save(self, data_type, id):
        with open(self._datasource, 'r') as f:
            read_data = json.loads(f.read())
            read_data[data_type].append(id)
            with open(self._datasource, 'w') as f:
                f.write(json.dumps(read_data))
        f.closed
