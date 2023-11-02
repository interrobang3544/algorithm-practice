while 1:
    stack = []
    str = input()

    if str == ".":
        break

    for letter in str:
        if letter == "[" or letter == "(":
            stack.append(letter)

        if letter == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(letter)

        if letter == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(letter)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
