T = int(input())

for i in range(T):
    R, word = input().split()
    for j in word:
        print(j * int(R), end='')
    print()