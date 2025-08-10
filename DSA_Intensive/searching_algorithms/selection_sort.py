#!/usr/bin/python3
from bogosort import load_numbers
import sys


def selection_sort(values):
    first = 0
    sorted_list = []

    for value in range(0, len(values)): #we iterate through every elem except the first one
        print(first)
        if values[value] < values[first]:
            values[first] = values[value]
        sorted_list.append(value)
    return sorted_list #returns a list of the position instead of the values

unsorted_list = load_numbers(sys.argv[1])

sorted_list = selection_sort(unsorted_list)
print(sorted_list)