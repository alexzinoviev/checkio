

def index_power(array, n):
    length = len(array)-1
    for index, i in enumerate(array):
        if n > length:
            return "-1"
        if index == n:
            return i ** n


index_power([1, 2], 3)