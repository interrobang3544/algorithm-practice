N = int(input())
dot_list = []

for i in range(N):
    x, y = map(int, input().split())
    dot_list.append([y, x])

dot_list.sort()
for dot in dot_list:
    print(dot[1], dot[0])