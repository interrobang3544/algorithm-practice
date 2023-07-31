from sys import stdin

input = stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().rstrip().split()
    
    match command[0]:
        case 'push':
            stack.append(int(command[1]))
        case 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        case 'size':
            print(len(stack))
        case 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        case 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])