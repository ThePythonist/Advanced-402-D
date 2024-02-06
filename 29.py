import xmltodict

xml_data = open("payments.xml")
xml_dict = xmltodict.parse(xml_data.read())
root = xml_dict["employees"]
employees = root["employee"]
selected_employees = []

for i in employees:
    if int(i["age"]) < 30:
        selected_employees.append(i)

print(len(selected_employees))
