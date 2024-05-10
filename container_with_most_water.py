""" test """


def solve(nums, start, end, water=0):
    """t"""

    if start >= end:
        return water

    smallest = nums[start] if nums[start] < nums[end] else nums[end]
    calc = (end - start) * smallest
    water = water if water > calc else calc

    if nums[start] < nums[end]:
        return solve(nums, start + 1, end, water)

    return solve(nums, start, end - 1, water)


Container = list(map(int, input().split()))

print(solve(Container, 0, len(Container) - 1))
