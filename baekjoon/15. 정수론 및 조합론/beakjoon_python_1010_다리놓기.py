import math

t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  print(math.floor(math.factorial(m)//math.factorial(m-n)//math.factorial(n)))
