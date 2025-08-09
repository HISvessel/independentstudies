#!/usr/bin/python3

import random
import sys 


def load_numbers(file_name): #this function loads our numbers from a text file into a list
    numbers = []

    with open(file_name) as f:
        for number in f:
            numbers.append(int(number))
        return numbers

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    while not is_sorted(values):
        random.shuffle(values)
    return values

unsorted_numbers = load_numbers(sys.argv[1])
sorted_numbers = bogo_sort(unsorted_numbers)
print(unsorted_numbers)
print(sorted_numbers)
print(is_sorted(sorted_numbers))