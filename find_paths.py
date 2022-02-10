#!/usr/bin/python3
import pandas as pd
import numpy as np
import sqlite3
import random
from io import StringIO
engine = create_engine('sqlite:///imdb.db', echo = False)

##############
## TODO:
## * ensure find_person utilities return a single result
## * figure out why title_principals isn't showing the whole cast and what to do about it.
##   * ANSWER: It shows the headliners, and there isn't an alternative.
##     although I could use the title_crew to get writiers and directors.
## * 


# given two unique identifiers, find a path connecting them.
# Gary Oldman: nm0000198
# Michael Caine: nm0000323
gary = "nm0000198"
michael = "nm0000323"

conn = sqlite3.connect("imdb.db")
cursor = conn.cursor()

def try_except_int(substr):
    try:
        return(int(substr))
    except:
        return False

def is_id(str):
    head_format = str[0:2] == "tt" or str[0:2] == "nm"
    numb_format = try_except_int(str[2:])
    return(head_format and numb_format)

query_to_table = lambda q: lambda x: pd.read_sql(q.format(target = x), conn)

def find_person_id(person):
    data = find_person(person)
    return data['nconst']

def find_person(person):
    try:
        fields = "nconst, primaryName, birthYear, deathYear, primaryProfession"
        query = "SELECT {fields} FROM name_basics WHERE primaryName = \"{target}\""
        query = query.format(fields = fields, target = person)
        return pd.read_sql(query, conn)
    except:
        return find_person_id(random.choices([gary, michael]))

def data_from_person(person): # person is an nconst value
#    if not is_id(person):
#        person = find_person_id(person)
    query = "SELECT * FROM title_principals WHERE nconst = \"{target}\""
    query = query.format(target = person)
    return pd.read_sql(query, conn)

def data_from_title(title): # title is a tconst value
#    if not is_id(title):
#        title = find_title_id(title)
    query = "SELECT * FROM title_principals WHERE tconst = \"{target}\""
    query = query.format(target = title)
    return pd.read_sql(query, conn)

titles_from_person = lambda p: data_from_person(p)['tconst']
people_from_title = lambda p: data_from_title(p)['nconst']

def shared_titles(person1, person2):
    titles1 = titles_from_person(person1)
    titles2 = titles_from_person(person2)
    return np.intersect1d(titles1, titles2)

def shared_people(title1, title2):
    person1 = person_from_title(title1)
    person2 = person_from_title(title2)
    return np.intersect1d(person1, person2)


shared_titles(gary, michael)

#is_person = lambda node: node[0:1] == "nm"
#is_title = lambda node: node[0:1] == "tt"
#
#def step_forward(node):
#    if is_person(node):
#        return get_titles(node)
#    else:
#        return get_people(node)
#
#
#
#def find_path(start, end):
#    if is_person(start) ^ is_person(end):
#        fore = start
#    else:
#        fore = step_forward(start)
#    aft = step_forward(end)
#    if any(fore in aft):
#        return fore in aft
#
#def order_path():
#    pass
#
#def person_ratings():
#    """Take the ratings of the projects a person is associated with,
#    weight them by the number of ratings, and produce
#    """
#    titles = None # insert query here
#    ratings, votes = select(averageRating, numVotes).where(tconst in titles)
#    return weighted_rating(ratings, votes)
#
#
def weighted_rating(ratings, votes):
    return sum([r * v for r, v in zip(ratings, votes)]) / sum(votes)