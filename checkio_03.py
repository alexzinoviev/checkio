def checkio(array):
    length = len(array)
    if length >=1:
        last_element = array[-1]
        even_elements = array[::2]
        even_sum = 0
        for i in even_elements:
            even_sum = even_sum+i
        result = even_sum*last_element
        return result
    else:
        return 0


    """
        sums even-indexes elements and multiply at the last
    """
    #return 0





print(checkio([0, 1, 2, 3, 4, 5]))