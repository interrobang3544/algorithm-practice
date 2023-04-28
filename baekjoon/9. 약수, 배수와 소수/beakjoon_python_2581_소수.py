prime_num = [2]

for i in range(3, 10000):
  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      break
  else:
    prime_num.append(i)


M = int(input())
N = int(input())
num_list = []

for i in range(M, N+1):
  if i in prime_num:
    num_list.append(i)

if len(num_list) == 0:
  print(-1)
else:
  print(sum(num_list))
  print(num_list[0])