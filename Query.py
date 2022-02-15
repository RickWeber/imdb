#!/usr/bin/python3

class Query:
    base_url = "https://imdb-api.com/en/API"
    def __init__(self, type, id):
        self.type = type # e.g. "Name"
        self.id = id

    def __repr__(self) -> str:
        pass

    def run_query(self):
        url_components = [self.base_url, self.type, key, self.id]

    def connected_titles(self): # use only if self.is_person
        search_url_components = [base_url, "Name", key, self.id]
        r = requests.get("/".join(search_url_components))
        all_data = json.loads(r.content)
        titles = all_data['castMovies']
        return pd.json_normalize(titles)

    def connected_people(): # use only if self.is_title
        search_url_components = [base_url, "Title", key, self.id]
        r = requests.get("/".join(search_url_components))
        all_data = json.loads(r.content)
        fields = ['writerList', 'starList', 'directorList', 'actorList', ]
        people = reduce(update,map(lambda x: all_data[x], fields))
        return pd.json_normalize(people)

