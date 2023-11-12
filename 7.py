def average(*args):
    total = 0
    length = 0
    for i in args:
        total += i
        length += 1

    print(total / length)

    # avg = sum(args) / len(args)
    # print(avg)


average(10, 20, 30)
