def fibonacci(N):
    if N <= 1:
        ans = N
    else:
        ans = fibonacci(N-1) + fibonacci(N-2)
        
    return ans

print(fibonacci(int(input())))