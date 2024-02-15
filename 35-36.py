import csv


def write(filename, data):  # 35
    header = ["name", "score", "major"]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    print("Done Writing Data")


def read(filename):  # 36
    keyword = "computer"

    with open(filename, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for i in reader:
            if keyword in i[2].lower():
                print(i)


students = [
    ["Helia", 16, "Computer Engineering"],
    ["Ali", 18, "Accouting"],
    ["Nasrin", 17, "Electrical Engineering"],
    ["Kian", 17, "Computer Science"],
    ["Mahdi", 18, "MBA"],
]

# write("students.csv", students)
read("students.csv")



