#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        r = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        int_num = 0
        for i in roman_string:
            if i not in r.keys():
                return 0
            int_num += r[i]
        return int_num
    return (0)
