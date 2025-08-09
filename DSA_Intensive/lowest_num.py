#!/usr/bi/python3

"""this script contins a function that searches through a list
and finds the lowest element on the list

This exercise is an example of linear search performed in a list. In
contrast to other functions, this one intends to locate when the desired value
is unknown but we have the criteria to find the lowest possible number
in any given list"""

def find_the_lowest(a_list: list[int]) -> int:
    """this function takes a list and returns the lowest value
    contained inside of the list, if a number is repeated, the returned index
    is the last one."""

    minimum = a_list[0] #points to the first element of the list
    for index in a_list:
        if index < minimum:
            minimum = index
            found_key = [key for key, value in enumerate(a_list) if value == minimum]
            continue
    return (minimum, found_key)


a_list = [4, 17, 5, 6, 2]
b_list = ['c', ' ', 'i', 's', ' ', 'f', 'u', 'n']
c_list = [True, False, True, False, False, False, True]
d_list = [3, 4, -2, -6, -6, 18, 5, 5, 5, 7]

find_in_a = find_the_lowest(a_list)
find_in_b = find_the_lowest(b_list)
find_in_c = find_the_lowest(c_list)
find_in_d = find_the_lowest(d_list)

if __name__ == '__main__':
    try:
        print(f"The lowest value in {a_list} is: [{find_in_a}]")
        print(f"The lowest value in {d_list} is: [{find_in_d}]")
        print(f"The lowest value in {c_list} is: [{find_in_c}]")
        print(f"The lowest value in {b_list} is: [{find_in_b}]")
    except Exception as e:
        print(e)
