N, M = map(int, input().split())
num_list = list(map(int, input().split()))
res = 0

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            num_sum = num_list[i] + num_list[j] + num_list[k]
            if(num_sum <= M):
                res = max(res ,num_sum)

print(res)