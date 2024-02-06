import xmltodict

# XML data to be parsed
xml_data = open("flights.xml").read()

# Parse XML data into a dictionary
data_dict = xmltodict.parse(xml_data)

# Access the parsed data
root = data_dict['flights']
flights = root['flight']
selected_flights = []

for i in flights:
    if i["destination"].lower() == "paris":
        print(i)
