n = int(input())
apocalypse_num = []
i = 1

while n > 0:
  if str(i).count('666') >= 1:
    apocalypse_num.append(i)
    n -= 1
  i += 1

print(apocalypse_num[n-1])