#!/usr/bin/python3
import pandas as pd
import requests
import gzip
from sqlalchemy import create_engine

name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
title_akas = "https://datasets.imdbws.com/title.akas.tsv.gz"
title_basics = "https://datasets.imdbws.com/title.basics.tsv.gz"
title_crew = "https://datasets.imdbws.com/title.crew.tsv.gz"
title_episode = "https://datasets.imdbws.com/title.episode.tsv.gz"
title_principals = "https://datasets.imdbws.com/title.principals.tsv.gz"
title_ratings = "https://datasets.imdbws.com/title.ratings.tsv.gz"
tables = [name_basics, title_akas, title_basics, title_crew, title_episode, title_principals, title_ratings]

engine = create_engine('sqlite:///imdb.db', echo = False)

for i in range(len(tables)):
    name = str(tables[i])
    t = tables[i]
    req = requests.get(t)
    file_gz = gzip.decompress(req.text)
    file_text = ''.join(map(chr, file_gz))
    df = pd.read_csv(file_text, sep = "\t")
    df.to_sql(name, con=engine, if_exists='replace')
