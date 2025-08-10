#!/usr/bin/python3
from bogosort import load_numbers
import sys


def selection_sort(values):
    """this function called selection sort was my unique non guided attempt at writing
    the selection sort algorithm by description alone and not by tutorial. Somehow, I got
    the function to return the arranged order of the number's indices, but the values are not
    arranged. The values seem to repeat, for some reason. And I think I know why: 
    
    since this attempt did not have any nested loops, we are not iterating through two
    different values independently, and therefore, we cannot make a comparison between 
    items iteratively. It looks as though the items are always compared to the index pointed
    at by the 'first' object down below, hence, not giving us the desired output"""
    first = 0 #we select the index manually
    sorted_list = [] #an empty list is created and returned with the sorted values

    for value in range(0, len(values)): #we iterate through every elem except the first one
        if values[value] < values[first]:
            first = value #switching indeces instead of values
        sorted_list.append(value)
    return sorted_list #returns a list of the position instead of the values

unsorted_list = load_numbers(sys.argv[1])

sorted_list = selection_sort(unsorted_list)
print(sorted_list)