def find_message(text):
    upper_chars = ""
    for i in text:
        if i.isupper() == True:
            upper_chars += i
    return upper_chars



    # for char in s:
    #     if s.isupper() == True:
    #     upper_chars += char

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
print(find_message("hello world!"))
print(find_message("HELLO WORLD!!!"))