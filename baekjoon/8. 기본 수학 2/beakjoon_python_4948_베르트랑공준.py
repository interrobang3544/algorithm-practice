prime_num = [2]

for i in range(3, 123456*2):
  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      break
  else:
    prime_num.append(i)

while 1:
  n = int(input())

  if n == 0:
    break
  
  cnt = 0
  for num in prime_num:
    if n < num <= 2*n:
      cnt += 1

  print(cnt)