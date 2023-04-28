N = int(input())
M = sorted(list(map(int, str(N))), reverse = True)

for num in M:
    print(num, end ='')