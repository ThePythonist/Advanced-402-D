def func(*args):
    print(sum(args))


func(10, 20, 30, 40)


def func(**kwargs):
    print(kwargs)


students = ["amirali", "amirali", "parham", "shayan", "parsa", "farbod"]
func(teacher="sadeghi", students=students, level="advanced")
