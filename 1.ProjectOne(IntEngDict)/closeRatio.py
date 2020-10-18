import json

from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("data.json"))
reply = 'y'
while(reply == 'y'):
    def keyVal(key):
        key = key.lower()
        if key in data:
            return data[key]
        elif len(get_close_matches(key, data.keys()))>0:
            return f"Did you mean %s instead?" % get_close_matches(key, data.keys())[0]
        else:
            return "Word not found. Please check again!"

    key = input("Insert key word: ")
    answer = keyVal(key)
    print(answer)
    reply = input("Do you want to continue?")
    reply.lower()