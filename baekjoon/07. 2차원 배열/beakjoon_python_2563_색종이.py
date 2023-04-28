n = int(input())
drawing_paper = [[0 for i in range(100)] for i in range(100)]

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(10):
    for j in range(10):
      drawing_paper[x+i][y+j] = 1


cnt = 0
for i in range(100):
  cnt += drawing_paper[i].count(1)

print(cnt)