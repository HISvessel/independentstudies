#!/usr/bin/python3
import time
#Let's now learn code

"""Example 1"""
def linear_search(a_list, target):
    """this list searches for the positional value
    in linear way of a given list
    
    Returns the index of the target position if found, else None"""

    for x in range(0, len(a_list)):
        if a_list[x] == target:
            return x
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}.")
    else:
        print("Target not found.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = time.time()
result = linear_search(numbers, 2)
end = time.time()
verify(result)
print(f"This operation took {end - start} time")