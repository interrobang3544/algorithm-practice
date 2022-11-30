import math

n = int(input())
num, num2 = [], []

for i in range(n):
  num.append(int(input()))
  num.sort(reverse=True)

for i in range(len(num) - 1):
    num2.append(num[i] - num[i+1])

greatest_common_divisor = math.gcd(*num2)
ans = [greatest_common_divisor]

for i in range(2, int(greatest_common_divisor ** 0.5) + 1):
  if greatest_common_divisor % i == 0:
    ans.extend([i, greatest_common_divisor//i])
    
print(*sorted(list(set(ans))))