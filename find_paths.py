#!/usr/bin/python3
import pandas as pd
from sqlalchemy import create_engine, select
from io import StringIO
engine = create_engine('sqlite:///imdb.db', echo = False)

# given two unique identifiers, find a path connecting them.
# Gary Oldman: nm0000198
# Michael Caine: nm0000323
gary = "nm0000198"
michael = "nm0000323"

with engine.begin() as connection:
    query1 = select(title_principals).where(title_principals.c.nconst == gary)
    title_set1 = connection.execute(query1)

is_person = lambda node: node[0:1] == "nm"
is_title = lambda node: node[0:1] == "tt"

def step_forward(node):
    if is_person(node):
        return get_titles(node)
    else:
        return get_people(node)



def find_path(start, end):
    if is_person(start) ^ is_person(end):
        fore = start
    else:
        fore = step_forward(start)
    aft = step_forward(end)
    if any(fore in aft):
        return fore in aft

def order_path():
    pass

def person_ratings():
    """Take the ratings of the projects a person is associated with,
    weight them by the number of ratings, and produce
    """
    titles = None # insert query here
    ratings, votes = select(averageRating, numVotes).where(tconst in titles)
    return weighted_rating(ratings, votes)


def weighted_rating(ratings, votes):
    return sum([r * v for zip(ratings, votes)]) / sum(votes)
