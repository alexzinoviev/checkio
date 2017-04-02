# "Fizz Buzz", если число делится на 3 и 5;
# "Fizz", если число делится на 3;
# "Buzz", если число делится на 5;
# Число, как строку для остальных случаев.
# Входные данные: Число, как целочисленное (int).
# Выходные данные: Ответ, как строка (str).
# Предусловия: 0 < number ≤ 1000


def input_value(number):
    return input(number)


def check_number():
    while True:
        try:
            value = int(input_value("Enter value:"))
            if 0 < value <= 1000:
                return value
            else: print("Value out of range, Please retry")
        except: ValueError ("Not a number, please retry")
        continue



def devide_values():
    value = check_number()
    x = value%3
    y = value%5
    return x,y,value

def results():
    x,y,value = devide_values()
    if x == y == 0:
        return print("Fizz Buzz")
    elif x == 0:
        return print("Fizz")
    elif y == 0:
        return print("Buzz")
    else:
        return print(str(value))


results()