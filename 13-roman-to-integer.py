# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:41:06 2020

@author: Faysal
Problem: https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        roman_value = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
            }

        i = 0
        num = 0

        while i < len(s):
            if (i + 1) < len(s) and s[i:i+2] in roman_value:
                num = num + roman_value[s[i:i+2]]
                i += 2
            else:
                num = num + roman_value[s[i]]
                i += 1
        return num