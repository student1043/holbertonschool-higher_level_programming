#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for i in range(len(new_list)):
        x += new_list[i]
    return (x)
