import json

from difflib import get_close_matches

data = json.load(open("data.json"))
reply = 'y'
while(reply == 'y'):
    def keyVal(key):
        key = key.lower()
        if key in data:
            return data[key]
        elif len(get_close_matches(key, data.keys())) > 0:
            rep = input(f"Did you mean {get_close_matches(key, data.keys())[0]} instead? Press Y for yes and N for no: ")
            rep.upper()
            if rep == 'Y':
                return data[get_close_matches(key, data.keys())[0]]
            elif rep == "N":
                return "Word not found. Please check again!"
            else:
                return "We didn't understand the entry."
        else:
            return "Word not found. Please check again!"

    key = input("Insert key word: ")
    answer = keyVal(key)
    print(answer)
    reply = input("Do you want to continue?")
    reply.lower()