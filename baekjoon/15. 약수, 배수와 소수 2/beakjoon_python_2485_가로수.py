from sys import stdin
from math import gcd

input = stdin.readline

n = int(input())
location = [int(input()) for _ in range(n)]
length = [location[i + 1] - location[i] for i in range(len(location) - 1)]

g = gcd(*length)

print(sum([len // g - 1 for len in length]))
