def checkio(*args):
    list = []
    min_element = ""
    max_element = ""
    for x in args:
        list.append(x)
        list.sort()
        min_element = list[0]
        max_element = list[-1]
    if list == []:
        return 0
    else:
        difference = max_element - min_element
        return difference




   # return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     def almost_equal(checked, correct, significant_digits):
#         precision = 0.1 ** significant_digits
#         return correct - precision < checked < correct + precision
checkio()

    # assert almost_equal(checkio(1, 2, 3), 2, 3)
    # assert almost_equal(checkio(5, -5), 10, 3)#, "5-(-5)=10"
    # assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3)#, "10.2-(-2.2)=12.4"
    # assert almost_equal(checkio(), 0, 3)#, "Empty"

#
# Давайте поработаем с числами.
# Дан массив чисел (float или/и int). Вам нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Ваша функция должна уметь работать с неопределенным количеством аргументов. Если аргументов нет, то функция возвращает 0 (ноль).
# Числа с плавающей точкой представлены в компьютерах как двоичная дробь. Результат проверяется с точностью до третьего знака, как ±0.001
# Прочитайте о том как работать с переменым числом аргументов.