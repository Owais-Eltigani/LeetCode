""" p """


def two_sum(nums, start, end, target):
    if start > end:
        return []

    if nums[start] + nums[end] == target:
        return [start + 1, end + 1]

    if nums[start] + nums[end] < target:
        return two_sum(nums, start + 1, end, target)

    if nums[start] + nums[end] > target:
        return two_sum(nums, start, end - 1, target)


nums = list(map(int, input().split()))
target = int(input())

print(two_sum(nums, 0, len(nums) - 1, target))
