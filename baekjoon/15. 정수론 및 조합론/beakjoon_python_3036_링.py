import math

n = int(input())
diameter = list(map(int, input().split()))

for i in range(1, n):
  gcd = math.gcd(diameter[0], diameter[i])
  print(f'{diameter[0]//gcd}/{diameter[i]//gcd}')