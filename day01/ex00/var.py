def my_var():
    for elem in [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]:
        print("{0} is of type {1}".format(elem, type(elem)));

if __name__ == '__main__':
    my_var()
