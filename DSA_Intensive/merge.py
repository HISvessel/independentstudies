#!/usr/bin/python3
from singly_linked_list import Node, LinkedList

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
