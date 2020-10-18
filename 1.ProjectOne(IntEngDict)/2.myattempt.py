# This section shows how to handle close enough words inserted by the user.
# It also makes it in lower case to match what exists in the database.
import json

from difflib import get_close_matches

data = json.load(open('data.json'))
def findMeaning(word):
    word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8))>0:
        match_list = get_close_matches(word, data.keys(),cutoff = 0.8)
        return data[match_list[0]]
    else:
        return "Word doesn't exist in database!"

print(findMeaning("brainn"))
