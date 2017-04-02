def checkio(words):
    splitted_words = words.split(" ")
    counter = 0
    for word in splitted_words:
        if word.isalpha() ==True:
            counter +=1
            if counter == 3:
                break
        else:
            counter = 0
            continue
    if counter == 3:
        return print("True")
    else:
        return print("False")

    #return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
#checkio("Hello World hello") == True, "Hello"
#checkio("He is 123 man")# == False, "123 man"
#checkio("1 2 3 4") #== False, "Digits"
#checkio("bla bla bla bla")# == True, "Bla Bla"
#checkio("Hi")# == False, "Hi"
checkio("one two 3 four five six 7 eight 9 ten eleven 12")