""" given an array of integers, return indices of the two numbers such that they add up to a specific target."""


def two_sum(nums, target):
    dict = {}

    for i in range(len(nums)):
        dict[nums[i]] = i

    for i in range(len(nums)):
        key = target - nums[i]

        if key in dict:
            return [i, dict[key]]
        else:
            continue

    return []


nums = list(map(int, input().split()))
target = int(input())

print(two_sum(nums, target))


""" 

A better solution is to iterate only once in the array and add to the empty dict and check if it there
that because addition is exchangable operation 3 + 5 == 5 + 3

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
