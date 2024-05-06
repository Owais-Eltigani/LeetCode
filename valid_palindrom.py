""" test """


def clean(string: str):

    string = string.replace(" ", "")

    for s in ["@", ":", "*", "#", ","]:
        if s in string:
            string = string.replace(s, "")

    return string.lower()


def solve(str, start, end):
    if start >= end:
        return True

    if str[start] != str[end]:
        return False

    return solve(str, start + 1, end - 1)


word = input()

word = clean(word)


print(solve(word, 0, len(word) - 1))
