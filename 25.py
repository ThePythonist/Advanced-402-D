import json

f1 = open("payments.json")
data = json.load(f1)

for emp in data["employees"]:
    print(emp["name"],":",emp["job_title"])
