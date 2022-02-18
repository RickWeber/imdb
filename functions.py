#!/usr/bin/python3
import pandas as pd
import sqlalchemy as sql

titles = list() # get list of titles from database
# Query constructor

def isTitle(item):
    # if it's already properly encoded, go for it, otherwise, pass the item to a search function and find an id value.
    if item in titles:
        return True
    return False

