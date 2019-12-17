#!/usr/bin/python3
for alpha_letters in range(122, 96, -1):
    if alpha_letters % 2 != 0:
        alpha_letters = alpha_letters - 32
    print("{:c}".format(alpha_letters), end="")
