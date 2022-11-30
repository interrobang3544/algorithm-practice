def check_prime(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    if a == 1:
        return False
    return True


T = int(input())

for i in range(T):
    n = int(input())
    for num in range(n // 2, 1, -1):
        if check_prime(num) and check_prime(n - num):
            print(num, n - num)
            break