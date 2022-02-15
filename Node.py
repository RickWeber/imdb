#!/usr/bin/python3
from people import get_person_title_data
from functools import reduce


class Node:
    base_url = "https://imdb-api.com/en/API"
    def __init__(self,id):
        self.id = id
        self.is_person = id[0:2] == "nm"
        self.is_title = id[0:2] == "tt"

    def on_paths(self):
        pass

    def find_path_to(self,node):
        pass

    def connected_nodes(self):
        if self.is_person:
            return self.connected_titles()
        else:
            return self.connected_people()

    def connected_titles(self): # use only if self.is_person
        search_url_components = [self.base_url, "Name", key, self.id]
        r = requests.get("/".join(search_url_components))
        all_data = json.loads(r.content)
        titles = all_data['castMovies']
        return pd.json_normalize(titles)

    def connected_people(): # use only if self.is_title
        search_url_components = [self.base_url, "Title", key, self.id]
        r = requests.get("/".join(search_url_components))
        all_data = json.loads(r.content)
        fields = ['writerList', 'starList', 'directorList', 'actorList', ]
        people = reduce(update,map(lambda x: all_data[x], fields))
        return pd.json_normalize(people)

    def people_intersect(self.id,nm2):
        titles1 = get_person_title_data(self.id)[['id','title','year']]
        titles2 = get_person_title_data(nm2)[['id','title','year']]
        return pd.merge(titles1, titles2, how = "inner")


# Find common titles between two people
