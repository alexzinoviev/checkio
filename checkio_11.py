def checkio(data):
    my_list = data
    new_list = my_list.copy()
    length = len(my_list)
    for i in range(length):
        f = True
        for j in range(length):
            if my_list[i] == my_list[j] and i != j:
                f = False
        if f == True:
            new_list.remove(my_list[i])
    return new_list



    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.

    #replace this for solution


print(checkio([1, 2, 3, 1, 3]))
print(checkio([1, 2, 3, 4, 5]))
print(checkio([5, 5, 5, 5, 5]))
print(checkio([10, 9, 10, 10, 9, 8]))