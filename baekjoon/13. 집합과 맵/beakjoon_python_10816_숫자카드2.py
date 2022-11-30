import sys

n = int(sys.stdin.readline().strip())
num_card = list(map(int, sys.stdin.readline().strip().split()))
num_count = {}

for num in num_card:
  if num in num_count:
    num_count[num] += 1
  else:
    num_count[num] = 1

m = int(sys.stdin.readline().strip())
num_check = list(map(int, sys.stdin.readline().strip().split()))

print(' '.join(str(num_count[num]) if num in num_count else '0' for num in num_check))