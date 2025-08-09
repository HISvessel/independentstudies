#!/usr/bin/python3

"""this script contains the function bubble sort, which sorts the
elemnt of an unsorted list by going through every value and rotating one number
at a time."""


import time

def ascending_bubble_sort(a_list):
    """this version of bubble sort function sorts the items from the smallest number
    to the largest one in an unsorted list. """
    length = len(a_list)
    for first in range(length - 1): #we iterate through the range of the list to point to the first comparable item
        for second in range(length - first - 1): #we nest loops in order to obtain the second value
            if a_list[second] > a_list[second + 1]: #if current is higher than the next value pointer to
                a_list[second], a_list[second + 1] = a_list[second + 1], a_list[second] #we reassign the current and next values

def descending_bubble_sort(a_list):
    """this version of bubbble sort somehow sorts the list in a descending order,
    going from the largest number to the smallest"""
    length = len(a_list)
    for first in range(length): #we iterate through the range of the list to point to the first comparable item
        for second in range(length): #we nest loops in order to obtain the second value
            if a_list[first] > a_list[second]: #if current is higher than the next value pointer to
                a_list[first], a_list[second] = a_list[second], a_list[first] #we reassign the current and next values




first_list = [3, 15, 4, 9, 10, 32]
second_list = [58, -1, 34, 23, 9, 8]
third_list = [7, 12, 9, 11, 3]

start_first = time.time()
bubble_one = ascending_bubble_sort(first_list)
end_first = time.time()

start_second = time.time()
bubble_two = ascending_bubble_sort(second_list)
end_second = time.time()

start_third = time.time()
bubble_three = ascending_bubble_sort(third_list)
end_third = time.time()

print(f"{first_list} took {end_first - start_first} seconds to bubble sort")
print(f"{second_list} took {end_second - start_second} seconds to bubble sort")
print(f"{third_list} took {end_third - start_third} seconds to bubble sort")

print()
print("-" * 20)
print()

start_first = time.time()
descending_bubble_one = descending_bubble_sort(first_list)
end_first = time.time()

start_second = time.time()
descending_bubble_two = descending_bubble_sort(second_list)
end_second = time.time()

start_third = time.time()
descending_bubble_three = descending_bubble_sort(third_list)
end_third = time.time()

print(f"{first_list} took {end_first - start_first} seconds to bubble sort")
print(f"{second_list} took {end_second - start_second} seconds to bubble sort")
print(f"{third_list} took {end_third - start_third} seconds to bubble sort")