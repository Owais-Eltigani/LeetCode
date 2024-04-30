""" given an array """


def find_biggest(arr: list[int]):
    """test"""

    biggest = 0

    for i in range(len(arr)):
        if arr[i] > arr[biggest]:
            biggest = i

    return biggest


def k_frequent(nums, k):
    """test"""

    max_element = max(nums)

    arr = [0] * (max_element + 1)

    for num in nums:
        arr[num] += 1

    biggest = []

    for _ in range(k):
        m = find_biggest(arr)
        biggest.append(m)
        arr[m] = 0

    return biggest


nums_arr = list(map(int, input().split()))
t = int(input())

print(k_frequent(nums_arr, t))
