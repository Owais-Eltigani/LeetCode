""" given an array of strings find all anagrams and put them in arrays togather """

from collections import defaultdict


def grouped_anagrams(words):
    """
    O(m * nlogn ) where m is the length of the initial list and that happen because we sort each word
    """

    dict = {}

    for word in words:
        s_word = "".join(sorted(word))

        if s_word in dict:
            dict[s_word].append(word)
        else:
            dict[s_word] = [word]

    return [values for values in dict.values()]


def optimum_solution(words):
    """
    a better approach to solve this problem is not to sort the words but to build ascii dictionary
    which can be used as map to see if the word ocurred before
    has much better time complexity O(m * n)
    """

    dict = defaultdict(list)

    for word in words:
        count = [0] * 26  # ? making list contain 26 element (alphabet)

        for letter in word:
            count[ord(letter) - ord("a")] = 1

        dict[tuple(count)].append(word)

    return list(dict.values())


strings = list(map(str, input().split()))

# print(grouped_anagrams(strings))
print(optimum_solution(strings))
