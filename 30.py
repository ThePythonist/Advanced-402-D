import xmltodict

xml_data = open("payments.xml")
xml_dict = xmltodict.parse(xml_data.read())
root = xml_dict["employees"]
employees = root["employee"]
python_salaries = []

for i in employees:
    if i["job_title"] == "Python Developer":
        for j in i["monthly_payment"].values():
            python_salaries.append(int(j))

avg = sum(python_salaries) / len(python_salaries)
print(avg)
