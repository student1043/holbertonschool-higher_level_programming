#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            num = my_list_1[index] / my_list_2[index]
        except IndexError:
            print("out of range")
            num = 0
        except (ValueError, TypeError):
            print("wrong type")
            num = 0
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        finally:
            new_list.append(num)
    return(new_list)
