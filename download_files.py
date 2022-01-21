#!/usr/bin/python3
import pandas as pd
import requests
import gzip

name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
title_akas = "https://datasets.imdbws.com/title.akas.tsv.gz"
title_basics = "https://datasets.imdbws.com/title.basics.tsv.gz"
title_crew = "https://datasets.imdbws.com/title.crew.tsv.gz"
title_episode = "https://datasets.imdbws.com/title.episode.tsv.gz"
title_principals = "https://datasets.imdbws.com/title.principals.tsv.gz"
title_ratings = "https://datasets.imdbws.com/title.ratings.tsv.gz"
tables = [name_basics, title_akas, title_basics, title_crew, title_episode, title_principals, title_ratings]

for t in tables:
    req = requests.get(t)
    file_gz = gzip.decompress(req.text)
    file_text = ''.join(map(chr, file_gz))
    df = pd.read_csv(file_text, sep = "\t")
    
