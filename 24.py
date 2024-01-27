import json

f1 = open("states.json")
data = json.load(f1)
selected = []

for i in data["states"]:
    if i["name"].lower() in ["alaska", "new york", "florida"]:
        selected.append(i)

f2 = open("selected_states.json", "w")
json.dump(selected, f2, indent=4)
