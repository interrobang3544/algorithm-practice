import sys
input = sys.stdin.readline

stack = []

n = int(input())
for _ in range(n):
    order = input()
    match int(order[0]):
        case 1:
            stack.append(order.split()[1])
        case 2:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop(-1))
        case 3:
            print(len(stack))
        case 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        case 5:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])