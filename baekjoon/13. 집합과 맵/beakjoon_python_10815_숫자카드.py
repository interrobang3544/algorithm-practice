import sys

N = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for i in range(len(card_list)):
    card_dict[card_list[i]] = 0

for j in range(M):
    if check_list[j] not in card_dict:
        print(0, end=' ')
    else:
        print(1, end=' ')