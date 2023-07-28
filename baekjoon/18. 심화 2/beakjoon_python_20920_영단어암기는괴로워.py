from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())
memorize = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in memorize:
            memorize[word][0] += 1
        else:
            memorize[word] = [1, len(word), word]

for word in sorted(memorize, key=lambda x:(-memorize[x][0], -memorize[x][1], memorize[x][2])):
    print(word)