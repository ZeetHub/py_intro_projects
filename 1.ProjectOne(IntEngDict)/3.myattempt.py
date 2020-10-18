# After looking for close enough words that look similar to what is inserted by the user...
# the program asks the user if he meant that close enough word...
import json

from difflib import get_close_matches

data = json.load(open('data.json'))
def findMeaning(word):
    word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8))>0:
        match_list = get_close_matches(word, data.keys(),cutoff = 0.8)
        reply = input("Did you mean %s? Reply 'y' for yes and 'n' for no: " %match_list[0])
        reply = reply.capitalize()
        if reply == 'Y':
            return data[match_list[0]]
        else:
            return "Word not found."
    else:
        return "Word not found."

print(findMeaning("brainn"))
