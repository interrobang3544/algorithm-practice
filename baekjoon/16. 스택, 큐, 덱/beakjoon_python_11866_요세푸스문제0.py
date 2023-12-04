import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
people = deque([i for i in range(1, n + 1)])
josephus = []

for i in range(n):
    for j in range(k):
        people.append(people.popleft())
    josephus.append(people.pop())

print(f'<{", ".join(map(str, josephus))}>')
