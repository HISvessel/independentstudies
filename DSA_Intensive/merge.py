#!/usr/bin/python3
from singly_linked_list import Node, LinkedList
import time

"""this script has tasks tohelp us better understand merge sorts. This is
our true beginning into Algorithms. The approach to this form of merge sort is
known as divide and conquer, and it relies on recursion as opposed to iteration
or traversion"""


def merge_sort(a_list):
    """sorts the given list in ascending order
    Does not sort in place, it will pass a new list"""
    #first step: divide, find the middle and divide into sublists
    if len(a_list) <= 1:
        return a_list
    L, R = split(a_list)
    left = merge_sort(L)
    right = merge_sort(R)
    #second step: recursively sort the sublist created first
    #thid step: combine the sorted sublist

    return merge(left, right)


def split(a_list):
    """divide the unsorted list at mid point into   sublist"""
    mid = len(a_list)//2
    left = a_list[:mid]
    right = a_list[mid:]
    return left, right

def merge(list1, list2):
    """this function merges two lists, sorting them in the process"""
    new_list = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(list1) and right_idx < len(list2):
        if list1[left_idx] < list2[right_idx]:
            new_list.append(list1[left_idx])
            left_idx += 1
        else:
            new_list.append(list2[right_idx])
            right_idx += 1
    while left_idx < len(list1):
        new_list.append(list1[left_idx])
        left_idx += 1
    while right_idx < len(list2):
        new_list.append(list2[right_idx])
        right_idx += 1
    return new_list

list1 = [54, 26, 62, 93, 17, 77, 31, 44, 55, 20]

start = time.time()
sorted_list = merge_sort(list1)
end = time.time()


print(f'{sorted_list} was merge sorted in {end - start} seconds.')