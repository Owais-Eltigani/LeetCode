""" test """


def solve(nums):
    """t"""

    uni = set(nums)
    long = []

    for num in uni:
        if num - 1 not in uni:
            i = 1

            while num + i in uni:
                i += 1

        long.append(i)

    return max(long)


nums = list(map(int, input().split()))


print(solve(nums))

""" 
[0,3,7,2,5,8,4,6,0,1]
"""
