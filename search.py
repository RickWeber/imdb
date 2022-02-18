#!/usr/bin/python3
"""Search utilities for the imdb database API"""
import requests
import pandas as pd
import json
from imdb import get_key
base_url = "https://imdb-api.com/en/API"
key = get_key()
# assemble search url
def make_url(keyword, query):
    search_url_components = [base_url, keyword, key, query]
    return "/".join(search_url_components)

# return data
def get_data(search_url):
    r = requests.get(search_url)
    results = pd.json_normalize(json.loads(r.content)['results'])
    return results

# Search functions
search = lambda q: get_data(make_url("Search", q))
search_title = lambda q: get_data(make_url("SearchTitle", q))
search_name = lambda q: get_data(make_url("SearchName", q))
# Note: search_name only returns 10 results

#def search_advanced(query):
#    query_components = [query,"count=250"]
#    search_url_components = [base_url, "AdvancedSearch", 
#    key, "&".join(query_components)]
#    search_url = "/".join(search_url_components)
#    return get_data(search_url)