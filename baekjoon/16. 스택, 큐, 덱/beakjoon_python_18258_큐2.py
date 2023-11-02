import sys
from collections import deque

input = sys.stdin.readline

queue = deque([])

n = int(input())
for _ in range(n):
    order = input().split()
    match (order[0], len(queue) == 0):
        case ("push", _):
            queue.append(int(order[1]))
        case ("pop", True):
            print(-1)
        case ("pop", False):
            print(queue.popleft())
        case ("size", _):
            print(len(queue))
        case ("empty", True):
            print(1)
        case ("empty", False):
            print(0)
        case ("front", True):
            print(-1)
        case ("front", False):
            print(queue[0])
        case ("back", True):
            print(-1)
        case ("back", False):
            print(queue[-1])
