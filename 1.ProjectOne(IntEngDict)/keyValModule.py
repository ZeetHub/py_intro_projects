data = ["pea", "rain", "train", "ordain"]

def keyVal(key):
    key = key.lower()
    if key in data:
        return data.count(key)
    else:
        return "Word not found. Please check again!"

key = input("Insert key word: ")
answer = keyVal(key)
print(answer)