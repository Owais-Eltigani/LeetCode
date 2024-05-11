""" test """


def prefix_postfix(nums):
    """q"""

    prefix = [0] * len(nums)
    postfix = [0] * len(nums)

    prefix_counter, post_counter = 0, 0

    for i in range(len(nums) - 1):
        prefix[i] = prefix_counter
        prefix_counter = prefix_counter if prefix_counter > nums[i] else nums[i]

        postfix[len(nums) - 1 - i] = post_counter
        post_counter = (
            post_counter
            if post_counter > nums[len(nums) - 1 - i]
            else nums[len(nums) - 1 - i]
        )

    return prefix, postfix


def solve2(nums):
    """t"""

    water_trapped = 0
    max_left, max_right = prefix_postfix(nums)

    for i in range(len(nums) - 1):
        calc = min(max_left[i], max_right[i]) - nums[i]
        water_trapped += calc if calc > 0 else 0

    return water_trapped


nums = list(map(int, input().split()))


print(solve2(nums))
