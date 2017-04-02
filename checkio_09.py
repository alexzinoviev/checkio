def checkio(str_number, radix):
    try:
        x = int(str_number, radix)
        return x
    except ValueError:
        return -1



    # return -1
#
#
print(checkio("AF", 16))
# checkio("101", 2) == 5, "Bin"
# checkio("101", 5) == 26, "5 base"
# checkio("Z", 36) == 35, "Z base"
print(checkio("AB", 10))

# print(int("AF", 16))
#
# print(int("101", 2))
#
# print(int("101", 5))
#
# print(int("Z", 36))
#
# print(int("AB", 10))