a, b = map(int, input().split())
c, d = map(int, input().split())

e = a * d + b * c
f = b * d

def gcd(e, f):
    while f:
        mod = f
        f = e % f
        e = mod
    return e

print(e//gcd(e, f), f//gcd(e, f))