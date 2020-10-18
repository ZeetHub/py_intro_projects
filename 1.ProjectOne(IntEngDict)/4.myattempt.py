# loop applied for the user to be able to request more that one word during the execution of the program
# out put made more user friendly
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

ask_word = 'Y'
while ask_word == 'Y':
    user_word = input("Enter a word: ")
    definition = findMeaning(user_word)
    if type(definition) == list:
        for item in definition:
            print(item)
    else:
        print(definition)
    ask_word = input("Do you want to continue? Reply 'y' for yes and 'n' for no: ")
    ask_word = ask_word.capitalize()
