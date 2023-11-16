import time

s1 = []
s2 = []


def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        runtime = t2 - t1
        print(f"Function {func.__name__} took {runtime} second to execute")
        print("-"*100)

        if func.__name__ == "solution1":
            s1.append(runtime)
        else:
            s2.append(runtime)

    return wrapper


@tictoc
def solution1():
    c = 0

    for i in range(50000):
        c += 1

    # print(c)


@tictoc
def solution2():
    c = 0

    while c < 50000:
        c += 1

    # print(c)


for i in range(10):
    solution1()
    solution2()

print(sum(s1) / len(s1))
print(sum(s2) / len(s2))
