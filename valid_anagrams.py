""" The valid anagrams problem is a problem that requires the user to determine if two strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. """


def check(str1, str2):
    if len(str1):
        if str1[0] == str2[0]:
            return check(str1[1:], str2[1:])
        else:
            return False

    return True


def valid_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    return check(str1, str2)


def valid_anagram2(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2


phrase1 = input()
phrase2 = input()

print(valid_anagram(phrase1, phrase2))
