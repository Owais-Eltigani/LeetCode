""" 
to solve leetcode problem contain duplicate numbers 
the statement of the problem is:
Given an array of integers, find if the array contains any duplicates.
"""

nums = list(map(int, input().split()))


def con_dup1(nums):
    """
    this makes use of a dictionary to store the numbers
    and check if the number is already in the dictionary
    O(n)
    """

    dict = {}

    for num in nums:
        if num in dict:
            return True
        dict[num] = 1

    return False


def con_dup2(nums):
    """this makes use of the set data structure to store the numbers and check if the number is already in the set"""
    return len(nums) != len(set(nums))


def con_dup3(nums):
    """this makes use of the sort function to sort the numbers and check if the number is equal to the previous number"""
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


print(con_dup2(nums))
