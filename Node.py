#!/usr/bin/python3
import pandas as pd
from people import get_person_title_data
from functools import reduce
import requests
import json

from imdb import get_key
base_url = "https://imdb-api.com/en/API"
key = get_key()

class Node:
    base_url = "https://imdb-api.com/en/API"
    def __init__(self,id,cache):
        self.id = id
        self.is_person = id[0:2] == "nm"
        self.is_title = id[0:2] == "tt"
        self.cache = cache

    def on_paths(self):
        pass

    def find_path_to(self,node):
        pass

    def neighbors(self):
        if self.neighbors:
            return self.neighbors
        if self.is_person:
            search_url_components = [self.base_url, "Name", key, self.id]
            r = requests.get("/".join(search_url_components))
            all_data = json.loads(r.content)
            titles = all_data['castMovies']
            self.neighbors = pd.json_normalize(titles)
        else:
            search_url_components = [self.base_url, "Title", key, self.id]
            r = requests.get("/".join(search_url_components))
            all_data = json.loads(r.content)
            fields = ['writerList', 'starList', 'directorList', 'actorList', ]
            people = reduce(dict.update,map(lambda x: all_data[x], fields))
            self.neighbors = pd.json_normalize(people)
        return self.neighbors

    def neighbors_of_neighbors(self):
        # I think this isn't going to work.
        return [n.neighbors for n in self.neighbors]

    def people_intersect(self.id, other_person):
        titles1 = get_person_title_data(self.id)[['id','title','year']]
        titles2 = get_person_title_data(other_person)[['id','title','year']]
        return pd.merge(titles1, titles2, how = "inner")
    


# Find common titles between two people
