matrix = []
max_num = 0
row = 0

for i in range(9):
  matrix.append(list(map(int,input().split())))

for i in range(9):
  max_num = max(max(matrix[i]), max_num)
  if max_num == max(matrix[i]):
    row = i

print(max_num)
print(row + 1, matrix[row].index(max_num) + 1)