def checkio(data):
    l = data
    l.sort()
    length = len(l)
    is_pair = length % 2
    med = length // 2
    if is_pair == 1:
        return l[med]
    elif is_pair == 0:
        value = (l[med] + l[med-1])/2
        return value



    #replace this for solution
    # return data[0]


checkio([1, 2, 3, 4, 5])

checkio([3, 1, 2, 5, 3])# == 3, "Not sorted list"
checkio([1, 300, 2, 200, 1])# == 2, "It's not an average"
checkio([3, 6, 20, 99, 10, 15])# == 12.5, "Even length"
checkio(list(range(1000000)))# == 499999.5