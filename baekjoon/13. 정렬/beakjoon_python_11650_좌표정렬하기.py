N = int(input())
dot_list = []
for i in range(N):
    x, y = map(int, input().split())
    dot_list.append([x, y])

dot_list.sort()
for dot in dot_list:
    print(dot[0], dot[1])