def checkio(number):
    s = str(number)
    l = []
    for i in s:
        if i!='0':
            l.append(int(i))
    multiple = 1
    for j in l:
        multiple*=j
    return multiple

print(checkio(123405))

print(checkio(999))
print(checkio(1000))
print(checkio(1111))