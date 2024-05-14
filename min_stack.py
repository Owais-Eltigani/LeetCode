""" design a stack DSA """


def push(stack, min_stack, num):
    if not stack:
        stack.append(num)
        min_stack.append(num)
        return

    smallest = min_stack[-1]
    min_stack.append(min(smallest, num))
    stack.append(num)


def pop(stack, min_stack):
    if not stack:
        return

    popped = stack.pop()
    _ = min_stack.pop()

    return popped


def get_min(min_stack):
    if not min_stack:
        return

    return min_stack[-1]


stack = []
min_stack = []

while True:
    command = input()

    match command:
        case "pop":
            print(pop(stack, min_stack))

        case "push":
            push(stack, min_stack, input())

        case "getMin":
            print(get_min(min_stack))

        case "Minstack":
            stack = []
            min_stack = []

        case _:
            break  # return
