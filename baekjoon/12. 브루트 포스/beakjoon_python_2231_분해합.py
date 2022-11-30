N = int(input())
res = 0

for i in range(1, N+1):        
    de_sum = i + sum(list(map(int, str(i))))              
    if(de_sum == N):                 
        res = i                   
        break

print(res)