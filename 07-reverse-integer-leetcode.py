# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:48:59 2020

@author: Faysal
Problem: https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int, rem=False) -> int: # added 'rem' a new parameter
        if x < 0:
            rem = True
            x = x * -1
        reve = 0
        while x > 0:
            y = x % 10
            reve = (reve * 10) + y
            x = x // 10
        if rem:
            reve *= -1
        max_range = (2 ** 31) - 1
        min_range = -2 ** 31
        
        if reve > max_range or reve < min_range:
            return 0
        else:
            return reve
        

        '''
        # Alternative solution
        
        if x < 0:
            res = int('-' + str(abs(x))[::-1])
        else:
            res = int(str(x)[::-1])
        
        if res > ((2 ** 31) - 1) or res < (-2 ** 31):
            return 0
        else:
            return res
        
        '''
        