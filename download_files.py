#!/usr/bin/python3
import pandas as pd
import requests
import gzip
from sqlalchemy import create_engine
from io import StringIO

# TODO: Make use of multiple threads to download/load faster
tables = {
"name_basics" : "https://datasets.imdbws.com/name.basics.tsv.gz",
"title_akas" : "https://datasets.imdbws.com/title.akas.tsv.gz",
"title_basics" : "https://datasets.imdbws.com/title.basics.tsv.gz",
"title_crew" : "https://datasets.imdbws.com/title.crew.tsv.gz",
"title_episode" : "https://datasets.imdbws.com/title.episode.tsv.gz",
"title_principals" : "https://datasets.imdbws.com/title.principals.tsv.gz",
"title_ratings" : "https://datasets.imdbws.com/title.ratings.tsv.gz"
}

engine = create_engine('sqlite:///imdb.db', echo = False)

for t in tables.keys():
    print("processing " + t)
    req = requests.get(tables[t])
    print("decompressing")
    file_gz = gzip.decompress(req.content)
    file_text = StringIO(''.join(map(chr, file_gz)))
    df = pd.read_csv(file_text, sep = "\t")
    print("adding to db")
    df.to_sql(t, con=engine, if_exists='replace')

print("done")