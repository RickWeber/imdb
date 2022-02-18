#!/usr/bin/python3
from imdb import get_key
base_url = "https://imdb-api.com/en/API"
key = get_key()

class Cache:
    def __init__(self, nodes, paths) -> None:
        self.data = None
        self.nodes = nodes
        self.paths = paths

    def check_cache(self, query):
        if self.query_has_run(query):
            pass
        elif self.query_intersect(query):
            pass
        else:
            self.add_to_cache(query)
            return query.run_query()
        pass

    def query_intersect(self, query):
        pass

    def add_to_cache(self, query):
        pass
