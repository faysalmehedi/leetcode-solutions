# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:36:28 2020

@author: Faysal
Problem: https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        temp = str(x)
        a = int(temp[::-1])
        return x == a
    
        # Alternative solution 
        # Without converting to string

#         if x < 0:
#             return False
#         else:
#             temp = x
#             reve = 0
#             while x > 0:
#                 y = x % 10
#                 reve = (reve * 10) + y
#                 x = x // 10

#             if temp == reve:
#                 return True
#             else:
#                 return False

