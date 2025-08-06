#!/usr/bin/python3
import time


def recursive_binary_search(a_list, target):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list)//2

        if a_list[midpoint] == target:
            return True
        else:
            if a_list[midpoint] < target:
                return recursive_binary_search(a_list[midpoint+1:], target)
            else:
                return recursive_binary_search(a_list[:midpoint], target)
            
def verify_result(result):
    print("Target found:", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
start = time.time()
result = recursive_binary_search(numbers, 12)
end = time.time()
verify_result(result)
print(f"This operation took {end - start} time")

start = time.time()
result = result = recursive_binary_search(numbers, 6)
end = time.time()
verify_result(result)
print(f"This operation took {end - start} time")
