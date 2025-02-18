import json

data={
    "a":1,
    "b":2,
    "c":3,
    "d":4
}

with open("xyz.json","w") as JSON_File:
    json.dump(data,JSON_File,indent=3)
    print("Data is written")

with open("xyz.json","r") as JSON_File:
    print(json.load(JSON_File))