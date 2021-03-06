#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
######################My solution##########################
def mergeLists(head1, head2):

    first_pointer = None
    current_pointer = None
    
    if head1 or head2:
        
        first_pointer, head1, head2 = next_pointer(head1, head2)
        current_pointer = first_pointer
    
        while head1 or head2:
            
            current_pointer.next, head1, head2 = next_pointer(head1, head2)
            current_pointer = current_pointer.next
            
    return first_pointer    

def next_pointer(head1, head2):
    print(head1)
    print(head2)
    tem_pointer = None
    
    if not head1:
        temp_pointer = head2
        head2 = head2.next
    elif not head2:
        print('here1')
        temp_pointer = head1
        head1 = head1.next     
    elif head1.data <= head2.data:
        temp_pointer = head1
        head1 = head1.next
    else:
        temp_pointer = head2
        head2 = head2.next
    

    print('temp pointer: ', temp_pointer)
    print('temp pointer next: ', temp_pointer.next)
    return temp_pointer, head1, head2


#################################################################
######################SOlution with dummy node####################

def mergeLists(head1, head2):

    first_pointer = SinglyLinkedListNode(0)
    current_pointer = first_pointer
        
    while(True):
        
        if not head1:
            current_pointer.next = head2
            break
        elif not head2:
            current_pointer.next = head1
            break   
        elif head1.data <= head2.data:
            current_pointer.next = head1
            head1 = head1.next
        else:
            current_pointer.next = head2
            head2 = head2.next
        
        current_pointer = current_pointer.next          
                 
    return first_pointer.next    
####################################################################




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
