# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:15:23 2020

@author: Faysal
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        current = head
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev