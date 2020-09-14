# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:22:36 2020

@author: Faysal
"""

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, value in enumerate(nums):
            remain = target - value
            if remain in checked:
                return [checked[remain], i]
            else:
                checked[value] = i
                
    '''
    alternate solution: working but takes too much time
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res = nums[i] + nums[j]
                if res == target:
                    return [i, j]
                    break
    
    '''