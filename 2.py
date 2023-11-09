from random import sample
from time import sleep
import os


def generate(length):
    password = [str(i) for i in sample(range(0, 10), length)]
    password = "".join(password)
    return password


counter = 0
time_left = 6  # Can be changed to any number

print(generate(6))
print("-" * 6)
while True:
    time_left -= 1
    sleep(1)
    print("Time Left :", time_left)

    if time_left == 0:
        os.system("cls")
        print(generate(6))
        print("-" * 6)
        time_left = 6
