N = int(input())
num_list = map(int, input().split())
prime_num = []

for num in num_list:
  if num == 1:
          continue
  for i in range(2, int(num ** 0.5) + 1 ):
      if num % i==0:
          break
  else:
    prime_num.append(num)

print(len(prime_num))