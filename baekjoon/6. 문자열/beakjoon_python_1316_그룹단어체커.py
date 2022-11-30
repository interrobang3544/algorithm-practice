N = int(input())
num = 0

for _ in range(N):
    word = input()
    cnt = 0

    for index in range(len(word) - 1):
        if word[index] != word[index + 1]:
            word2 = word[index + 1:]
            if word[index] in word[index + 1:]:
                cnt += 1

    if cnt == 0:
        num += 1

print(num)