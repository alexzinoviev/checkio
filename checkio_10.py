def checkio(numbers_array):
    l = list(numbers_array)
    l.sort(key=sort_without_symbols)
    return l


def sort_without_symbols(value):
    if value < 0:
        value = value*(-1)
    return value

#sort_without_symbols()


print(checkio((-20, -5, 10, 15)))

print(checkio((-1, -2, -3, 0)))
print(checkio((1, 2, 3, 0)))