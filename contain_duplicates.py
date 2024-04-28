""" to solve leetcode problem contain duplicate numbers 
the statement of the problem is:
Given an array of integers, find if the array contains any duplicates.
"""

nums = list(map(int, input().split()))


def solution1(nums):
    """this makes use of a dictionary to store the numbers and check if the number is already in the dictionary"""
    dict = {}

    for num in nums:
        if num in dict:
            return True
        dict[num] = 1

    return False


def solution2(nums):
    """this makes use of the set data structure to store the numbers and check if the number is already in the set"""
    return len(nums) != len(set(nums))


print(solution2(nums))
