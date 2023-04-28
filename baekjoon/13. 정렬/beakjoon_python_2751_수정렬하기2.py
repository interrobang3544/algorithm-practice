import sys

N = int(input())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))
num2 = sorted(num)

for i in num2:
    print(i)