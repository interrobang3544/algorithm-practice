n, m = map(int, input().split())
string_list = []

for i in range(n):
  string_list.append(input())

cnt = 0
for i in range(m):
  if input() in string_list:
    cnt += 1
  
print(cnt)