#!/usr/bin/python3
# A script using the imdb api (https://imdb-api.com/)
# to navigate the universe of what to watch.
import requests
import os
# API Connection details
def attempt_connection():
    if not exists('secret.config'):
        get_key_prompt()
    else:
        with os.open('secret.config') as file:
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
        attempt_connection()
# Functions to assemble api calls
def insert_key(api_call):
    return "https://imdb-api.com/en/" + key
def api_call():
    
def main():
    key = attempt_connection()
    # get call
    insert_key(make_call(input()))