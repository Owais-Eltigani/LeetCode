""" test """


def two_sum(nums, index, start, end):

    if start >= end:
        return []

    if index == start:
        return two_sum(nums, index, start + 1, end)

    if index == end:
        return two_sum(nums, index, start, end - 1)

    if nums[index] + nums[start] + nums[end] == 0:
        return [nums[index], nums[start], nums[end]].sort()

    if nums[index] + nums[start] + nums[end] < 0:
        return two_sum(nums, index, start + 1, end)

    if nums[index] + nums[start] + nums[end] > 0:
        return two_sum(nums, index, start, end - 1)


def solve2(nums):
    """e"""

    nums.sort()
    result = []

    for i in range(len(nums) - 1):
        res = two_sum(nums, i, 0, len(nums) - 1)

        if res and res not in result:
            result.append(res)

    return result


nums = list(map(int, input().split()))

print(solve2(nums))
