def fib(n):
  global fibCnt
  if n == 1 or n == 2:
    return 1  # 코드1
  else:
    fibCnt += 1
    return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
  global fibonacciCnt
  f = [0 for _ in range(n+1)]
  f[1], f[2] = 1, 1
  for i in range(3, n+1):
    fibonacciCnt += 1
    f[i] = f[i-1] + f[i-2]   
  return f[n]

n = int(input())
fibCnt, fibonacciCnt = 1, 0
fib(n)
fibonacci(n)
print(fibCnt, fibonacciCnt)