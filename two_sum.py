"""
given an array of integers, return indices of the
two numbers such that they add up to a specific target.
"""

class Solution(object):
    def twoSum(self, nums, target):
    """
    !this method has a O(n * 2) -> O(n) because we looping twice.
    first to build up the dictionary then to check the values against the dictionary
    """            
        dict = {}

        for i, num in enumerate(nums):
        dict[num] = i
        
        for i, num in enumerate(nums):
        key = target - num

        if key in dict:
            return [i, dict[key]]
                


""" 
A better solution is to iterate only once in the array 
and then add to the empty dict and check if it there
that because addition is exchangeable operation 3 + 5 == 5 + 3.

?this gives a O(n) because we iterate only once and we building the dict in the iteration

class Solution(object):
    def twoSum(self, nums, target):

        dict = {}
        
        for i,num in enumerate(nums):
            t = target - num

            if t in dict:
                return [i, dict.get(t)]
            else:
                dict[num] = i
                
"""
