"""
given an array of integers, return indices of the
two numbers such that they add up to a specific target.
"""


def two_sum(nums, target):
    """
    !this method has a O(n * 2) -> O(n) but we looping twice.
    first to build up the dictionary then to check the values against the dictionary
    """

    dict = {}

    for i, num in nums:
        dict[num] = i

    for i, num in nums:
        key = target - num

        if key in dict:
            return [i, dict[key]]

    return []


nums = list(map(int, input().split()))
target = int(input())

print(two_sum(nums, target))


""" 
A better solution is to iterate only once in the array 
and then add to the empty dict and check if it there
that because addition is exchangeable operation 3 + 5 == 5 + 3.

?this gives a O(n) because we iterate only once and we building the dict in the iteration

def solve(nums, target):
    dict = {}
    
    for index, num in nums:
        key = target - num
        
        if key in dict:
            return [index, dict[key]]
        else:
            dict[key] = index
    
    return []
"""
