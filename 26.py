# import json
#
# f1 = open("payments.json")
# data = json.load(f1)
# employees = {}
#
# for emp in data["employees"]:
#     emp_salary = [i for i in emp["monthly_payment"].values()]
#     avg = sum(emp_salary) / len(emp_salary)
#     # print(emp["name"], ":", avg)
#     employees.setdefault(emp["name"],avg)
#
# print(employees)

import time


for i in range(5):
    time.sleep(1)
    print(f"Hacking nasa in {5-i} seconds")

print("Congrats ! NASA is hacked")
