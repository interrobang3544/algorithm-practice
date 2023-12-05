import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
paper = deque(list(enumerate(map(int, input().split()))))
poped = []

while paper:
    index, num = paper.popleft()
    poped.append(index + 1)
    if num > 0:
        paper.rotate(-(num-1))
    else:
        paper.rotate(-num)
print(*poped)
