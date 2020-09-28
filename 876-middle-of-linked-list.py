# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:41:38 2020

@author: Faysal
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        # Finding the number of elements
        head1 = head
        count = 0
        
        while head1 != None:
            count += 1
            head1 = head1.next
        
        # Find the middle of the element number
        middle = count // 2
        
        # Another Loop for go to middle of the element
        head2 = head
        position = 0
        while position < middle:
            head2 = head2.next
            position += 1
        
        return head2