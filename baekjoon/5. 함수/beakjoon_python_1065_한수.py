def hansu(a):
    cnt = 0
    for i in range(1, a + 1):
        a = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif a[0] - a[1] == a[1] - a[2]:
            cnt += 1
    return cnt


N = int(input())
print(hansu(N))