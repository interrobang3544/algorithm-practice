import math

t = int(input())

for i in range(t):
  n = int(input())
  type_list = []
  type_count = []

  for j in range(n):
    cloth, type = input().split()

    if type not in type_list:
      type_list.append(type)
      type_count.append(2)
    else:
      type_count[type_list.index(type)] += 1
  
  ans = 1
  for k in range(len(type_count)):
    ans *= type_count[k]
  print(ans - 1)