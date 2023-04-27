n, m = map(int, input().split())
answer = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    for k in range((j-i)//2+1):
        answer[i-1+k], answer[j-1-k] = answer[j-1-k], answer[i-1+k]

print(' '.join(str(n) for n in answer))