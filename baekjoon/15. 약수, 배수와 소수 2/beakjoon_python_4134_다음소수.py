from sys import stdin

input = stdin.readline

test_case = int(input())

for i in range(test_case):
    n = int(input())

    while 1:
        if n == 0 or n == 1:
            print(2)
            break

        for i in range(2, int(n ** 0.5) + 1 ):
            if n % i == 0:
                break
        else:
            print(n)
            break
        n += 1