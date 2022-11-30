n, m = map(int, input().split())
a, b = set(list(map(int, input().split()))), set(list(map(int, input().split())))

print(len((a-b)|(b-a)))