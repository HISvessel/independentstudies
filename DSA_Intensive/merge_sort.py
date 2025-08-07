#!/usr/bin/python3
import time

def merge_sort(list1, list2):
    """the function returns a new sorted merged list of both given
    lists as function arguments.
    
    In easy mode, we use the python builtins to perform a simple merging
    with the .extend builtin and then sort the elements with sorted.
    
    In medium mode, we rely less on the builtins and simply concatenate lists
    together, and return them as a sorted version of the concatenation. The function
    is shorter, but still bypasses the concept of sorting for a more Pythonic function
    
    in hard mode, the intention will be to sort them manually, which 
    would result in a denser function with nested loops and conditioning."""
    #new_list = list1
    #new_list.extend(list2)
    #return sorted(new_list)
    new_list = list1
    return sorted(new_list + list2)

    


l1 = [1, 2, 4]
l2 = [1, 3, 4]

start = time.time()
new_list = merge_sort(l1, l2)
end = time.time()

print(f"Merging two lists: {l1} and {l2}")
print(new_list)
print(f"It took {end - start} time to merge both lists")
#time taken ranges between 1 second in best scenarios
#and 7 to 9 seconds in the worst of scenarios