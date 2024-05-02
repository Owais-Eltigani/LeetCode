""" 
pass
"""


def encode(arr):
    """
    pass
    """

    encoded_str = ""

    for string in arr:
        delimiter = str(len(string)) + "#"
        encoded_str = encoded_str + delimiter + string

    return encoded_str


def decode(string: str):
    """
    pass
    """

    decoded_str = []

    while True:
        start = string.find("#") + 1
        end = int(string[: start - 1]) + start

        decoded_str.append(string[start:end])
        string = string[end:]

        if len(string) <= 0:
            return decoded_str


strings = list(map(str, input().split(" ")))

enc = encode(strings)

print(enc)
print("after")
print(decode(enc))
