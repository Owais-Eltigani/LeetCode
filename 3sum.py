""" test """


def two_sum(nums, index, start, dict):

    if start >= len(nums) - 1:
        return []

    if index == start:
        return two_sum(nums, index, start + 1, dict)

    c = (nums[index] + nums[start]) * -1

    if nums[index] + nums[start] + c == 0 and c in dict:
        return [nums[index], nums[start], c]

    return two_sum(nums, index, start + 1, dict)


def solve2(nums):
    """e"""

    nums.sort()
    result = []
    dict = {num: 0 for num in nums}

    for i in range(len(nums) - 1):
        res = two_sum(nums, i, 0, dict)
        res.sort()

        if res and res not in result:
            result.append(res)

    return result


nums = list(map(int, input().split()))

print(solve2(nums))
