import json

f1 = open("states.json")
data = json.load(f1)
state_names = []
for i in data["states"]:
    state_names.append(i["name"])

