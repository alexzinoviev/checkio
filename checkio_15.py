NEWBORN = 10000

def fibonacci():
    fibo = [1]
    fibo1 = fibo2 = i = 1
    while i < 20:
        fib_sum = fibo2 + fibo1
        fibo1 = fibo2
        fibo2 = fib_sum
        i += 1
        fibo.append(fib_sum)
    return fibo


# def checkio(opacity):
#     x = NEWBORN
#     for i in range(1,5000):
#         if x != opacity:
#             if i in fibonacci():
#                 x = x - i
#             else:
#                 x = x + 1
#         else:
#             i = i-1
#             return i


def checkio(opacity):
    x = NEWBORN
    while x != opacity:
        for i in range(1,5000):
            if i in fibonacci():
                x = x - i
            else:
                x = x + 1
        break
        # else:
        #     i = i-1
        #     return i


#checkio(10000) == 0#, "Newborn"
#checkio(9999) == 1 #, "1 year"
# checkio(9997) == 2#, "2 years"
checkio(9994) == 3#, "3 years"
#checkio(9995) == 4#, "4 years"
print(checkio(9990)) == 5#, "5 years"