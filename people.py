#!/usr/bin/python3
"""Utilities for pulling data related to people"""
import requests
import pandas as pd
import json
from imdb import get_key
base_url = "https://imdb-api.com/en/API"
key = get_key()
base_url = "https://imdb-api.com/en/API"
# Get data for one person
def get_person_data(nm):
    search_url_components = [base_url, "Name", key, nm]
    r = requests.get("/".join(search_url_components))
    return json.loads(r.content)
# Get titles associated with one person
def get_person_title_data(nm):
    all_data = get_person_data(nm)
    titles = all_data['castMovies']
    return pd.json_normalize(titles)
# Find common titles between two people
def people_intersect(nm1,nm2):
    titles1 = get_person_title_data(nm1)[['id','title','year']]
    titles2 = get_person_title_data(nm2)[['id','title','year']]
    return pd.merge(titles1, titles2, how = "inner")
