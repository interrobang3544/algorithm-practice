n, m = map(int, input().split())

case = []
def recursive():
  if len(case) == m:
    print(' '.join(map(str, case)))
    return

  for i in range(1, n + 1):
    case.append(i)
    recursive()
    case.pop()

recursive()