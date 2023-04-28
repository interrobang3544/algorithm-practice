n = int(input())
body = []
body_rank = [1 for _ in range(n)]

for i in range(n):
  body.append(list(map(int, input().split())))

for i in range(n):
  for j in range(n):
    if (body[i][0] < body[j][0]) and (body[i][1] < body[j][1]):
      body_rank[i] += 1

for i in range(n):
  print(body_rank[i], end = ' ')