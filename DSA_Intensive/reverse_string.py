#!/usr/bin/python3

def reverse_string(str):
    for i in str[::-1]:
        print(i, end='')
    print()
        

str = ['h', 'e', 'l', 'l', 'o']

reverse_string(str)