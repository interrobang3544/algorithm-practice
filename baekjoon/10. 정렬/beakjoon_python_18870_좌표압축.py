import sys
N = int(input())

coord_list = list(map(int, sys.stdin.readline().split()))

coord_list_sorted = sorted(list(set(coord_list)))

coord_dict = {}
for i in range(len(coord_list_sorted)):
    coord_dict[coord_list_sorted[i]] = i

for i in coord_list:
    print(coord_dict[i], end=' ')