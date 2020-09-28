# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:41:03 2020

@author: Faysal
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while head is not None and head.val == val:
            head = head.next
            
        if head is None:
            return None
            
        temp = head
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head