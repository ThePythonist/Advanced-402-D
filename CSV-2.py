import csv


def write(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


def read(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row)


def add(filename, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'{filename} has been updated successfully.')


data1 = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'London'],
    ['Bob', '35', 'Paris']
]

data2 = [
    ['Mike', '40', 'Berlin'],
    ['Emily', '28', 'Tokyo']
]

# write("data.csv", data1)
# add("data.csv", data2)
# read("data.csv")
