""" finding if a group of parentheses  """


def solve(str):
    if not str:
        return True

    stack = []

    for c in str:
        if c in ["(", "{", "["]:
            stack.append(c)
        else:
            popped = stack.pop()

            if c == ")" and popped == "(":
                continue

            if c == "}" and popped == "{":
                continue

            if c == "]" and popped == "[":
                continue

            return False

    return len(stack) == 0


str = input()

print(solve(str))
