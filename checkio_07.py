def left_join(phrases):
    new_list = []
    for i in phrases:
        i = i.replace('right','left')
        new_list.append(i)
    new_str = ','.join(new_list)
    return new_str


#left_join(("left", "right", "left", "stop"))
print(left_join(("bright aright", "ok")))

print(left_join(("brightness wright",)))
print(left_join(("enough", "jokes")))
