#!/usr/bin/python3

from singly_linked_list import LinkedList


def merge_sort(linked_list):
    """this function merges a linked list in ascending order
    you recursively divide the linked list to have it contain a single
    node amd repeatedly merge"""
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """this function takes a linked lists and divides it into multiple
    sublists that contain only one element inside of every single list"""
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.index_at_position(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half

def merge(left, right):
    """this function merges two linked lists sorting by
    dqta in the nodes and it returns a new merged list"""
    #creae a new linked lists that contains
    #nodes merged left and right
    merged = LinkedList()

    #creating a fake head to discard later
    merged.add(0)

    #set current to the head of the linked list

    current = merged.head

    left_head = left.head
    right_head = right.head

    #iterates pver left and right until we reach the tail node of either

    while left_head or right_head:
        #if the left node of head is none, were past the tail
        #add the node form right to merged linked list
        if left_head is None:
            current.next_node = right_head
            #call next on right to set loop condition to false
            right_head = right_head.next_node
        # if head node of right is node, were past the tail
        #add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            #called next on left to set loop condition to false
            left_head = left_head.next_node
        #reached a node where either are 
        else:
            #not at either tail node
            #obtained node data to perrfrom cmparison
            left_data = left_head.data
            right_data  = right_head.data
            #if data on left is less than right
            #set current to the left node
            if left_data < right_data:
                current.next_node = left_head
                #move left head to next node
                left_head = left_head.next_node
            #if left data is higher, then set current to right node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        #move current to next node
        current = current.next_node
    #discard fake head and set first merged node as the head
    head = merged.head.next_node
    merged.head = head
    return merged


l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)