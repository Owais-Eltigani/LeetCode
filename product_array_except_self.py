""" 
find the the product of an array except self 
"""


def solve3(num):
    """
    O(n)
    """

    pre = [1] * (len(num) + 1)
    post = [1] * (len(num) + 1)

    for i in range(len(num)):
        rev = len(num) - i - 1

        pre[i + 1] = pre[i] * num[i]
        post[rev] = post[rev + 1] * num[rev]

    answer = []

    for i in range(len(num)):
        answer.append(pre[i] * post[i + 1])

    return num


nums = list(map(int, input().split()))

print(solve3(nums))
