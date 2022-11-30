t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        r1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        r2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5
        if (r1 < r and r2 > r) or (r1 > r and r2 < r):
            cnt += 1
    print(cnt)