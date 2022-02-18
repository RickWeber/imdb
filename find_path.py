#!/usr/bin/python3
import pandas as pd
from sqlalchemy import create_engine
import sys

start = sys.argv[1]
end = sys.argv[2]
if isTitle(start):
    startType = 'title'
else:
    startType = 'person'
if isTitle(end):
    endType = 'title'
else:
    endType = 'person'
