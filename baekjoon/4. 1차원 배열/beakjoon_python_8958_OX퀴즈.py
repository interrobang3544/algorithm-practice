N = int(input())

for i in range(N):
    result = list(input())
    count = 0
    score = 0

    for j in range(len(result)):
        if result[j] == 'O':
            count += 1
            score += count
        else:
            count = 0

    print(score)