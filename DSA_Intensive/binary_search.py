#!/usr/bin/python3
from linear_search import verify

def binary_search(a_list, target):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if a_list[midpoint] == target:
            return midpoint
        elif a_list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = binary_search(numbers, 7)

verify(result)