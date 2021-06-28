def average(array):
    return sum(array) / len(array)


def print_array_names(array):
    for _ in array:
        print(_.name, end=" ")
