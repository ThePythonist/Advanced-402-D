import random


def irancell():
    pn = ""
    code = random.choice(["0939", "0933", "0936"])
    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


def rightell():
    pn = ""
    code = random.choice(["0921", "0922", "0923"])
    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


def hamrahaval():
    pn = ""
    code = random.choice(["0993", "0919", "0911", "0912"])
    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


print("line 34 :", __name__)

if __name__ == "__main__":  # Yaani file be sorat mostaghim run shavad
    print(irancell())
    print(rightell())
    print(hamrahaval())
