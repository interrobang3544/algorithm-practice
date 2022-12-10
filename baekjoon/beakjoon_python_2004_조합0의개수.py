def countNum(target, num):
  cnt = 0 
  while target > 0:
    target //= num
    cnt += target
  print(cnt)
  return cnt


n, k = map(int, input().split())

count_two = countNum(n, 2) - countNum(k, 2) - countNum(n - k, 2)
count_five = countNum(n, 5) - countNum(k, 5) - countNum(n - k, 5)

print(min(count_two, count_five))