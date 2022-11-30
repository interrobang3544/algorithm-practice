n, m = map(int, input().split())
unheard = set([])
not_seen = set([])

for i in range(n):
  unheard.add(input())

for i in range(m):
  not_seen.add(input())

print(len(unheard & not_seen))

for name in sorted(list(unheard & not_seen)):
  print(name)