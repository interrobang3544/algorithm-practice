N = int(input())
N_origin = N
i = 0

while True:
    i += 1
    N1 = (N // 10) + (N % 10)
    N2 = ((N % 10) * 10) + (N1 % 10)

    if N2 == N_origin:
        break
    else:
        N = N2

print(i)