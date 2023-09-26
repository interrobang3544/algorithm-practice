import sys
input = sys.stdin.readline

stack = []

k = int(input())
for _ in range(k):
    num = int(input())
    match num == 0:
        case True:
            stack.pop()
        case False:
            stack.append(num)

print(sum(stack))