"""
given an array with duplicated elements and integer k donates
the number of returns. return the most k frequent elements 
"""


def find_biggest(arr: list[int]):
    """
    find the biggest element in array
    """

    biggest = 0

    for i in range(len(arr)):
        if arr[i] > arr[biggest]:
            biggest = i

    return biggest


def k_frequent(nums, k):
    """
    using a bucket like techniques to find the best element in the array then declaring
    another array with length k to initialized with 0s representing the occurrences
    runs on O(n + k * m) where:
    n := array given
    k := number of k elements to be returned
    m := number of elements in the frequency array which depends on the biggest element in nums
    """

    max_element = max(nums)

    arr = [0] * max_element + 1

    for num in nums:
        arr[num] += 1

    biggest = []

    for _ in range(k):
        m = find_biggest(arr)
        biggest.append(m)
        arr[m] = 0

    return biggest


def solve(nums, k):
    """
    create a dictionary then map the values by there occurrences [1,1,1,2,2,3] -> {1:3, 2:2, 3:1}
    then creating a frequency array mapping the values of dict to there indices
    has O(n)
    """
    count = {}
    frequency = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        frequency[c].append(n)

    k_elements = []

    for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
            if len(k_elements) != k:
                k_elements.append(n)

    return k_elements


nums_arr = list(map(int, input().split()))
t = int(input())

print(solve(nums_arr, t))
