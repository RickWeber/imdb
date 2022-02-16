#!/usr/bin/python3
# A script using the imdb api (https://imdb-api.com/)
# to navigate the universe of what to watch.
from msilib.schema import Class
import requests

def main():
    key = get_key()
    # get call
    insert_key(make_call(input()))

# API Connection details
def get_key():
    if not exists('secret.config'):
        get_key_prompt()
    else:
        with open('secret.config') as file:
            __ = file.readline()
            key = file.readline().strip()
            key = read(file).strip()
    return key

def get_key_prompt():
    print("I'm sorry, I can't find your API key."
    "You can get a key at https://imdb-api.com."
    "save in a text file named 'apikey' in this folder.")
    print("Would you like to go do that now and try this again? [Y]")
    print("Or would you prefer to exit now and try again later? [n]")
    quit_now = input("> ")
    if "n" in quit_now:
        quit()
    else:
        get_key()

# Functions to assemble api calls
def insert_key(api_call):
    return "https://imdb-api.com/en/" + key + api_call

    
def call_to_key(api_call):
    """given a valid API call, convert it to a string that can be used as a dictionary key."""
    api_call_key = str(api_call)
    return api_call_key

def check_cache(api_call, cache):
    call_to_key(api_call)
    if cache[api_call]