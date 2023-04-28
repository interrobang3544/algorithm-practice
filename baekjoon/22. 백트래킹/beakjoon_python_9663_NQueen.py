def isPromising(x):
  for i in range(x):
    if (chess_table[x] == chess_table[i]) or (x - i == abs(chess_table[x] - chess_table[i])):
      return 0
  return 1

def nqueen(x):
  global cnt
  if x == n:
    cnt += 1
    return
  for i in range(n):
    chess_table[x] = i
    print(chess_table)
    if isPromising(x) == 1:
      nqueen(x + 1)

n = int(input())
chess_table = [0 for _ in range(n)]
cnt = 0
nqueen(0)
print(cnt)