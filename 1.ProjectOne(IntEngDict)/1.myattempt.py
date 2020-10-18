import json

data = json.load(open('data.json'))

def findMeaning(word):
    if word in data:
        return data[word]
    else:
        return "Word doesn't exist in database!"

print(findMeaning("brainn"))
