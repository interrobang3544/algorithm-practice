def factorial(N):
    ans = 1
    
    if N > 0 :
        ans = N * factorial(N-1)
        
    return ans

print(factorial(int(input())))