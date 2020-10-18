import json

data = json.load(open("data.json"))
reply = 'y'
while(reply == 'y'):
    def keyVal(key):
        key = key.lower()
        if key in data:
            return data[key]
        else:
            return "Word not found. Please check again!"

    key = input("Insert key word: ")
    answer = keyVal(key)
    print(answer)
    reply = input("Do you want to continue?")
    reply.lower()