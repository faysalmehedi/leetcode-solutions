# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:03:36 2020

@author: Faysal
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        
        while head != None:
            count = 2 * count + head.val
            head = head.next
            
        return count