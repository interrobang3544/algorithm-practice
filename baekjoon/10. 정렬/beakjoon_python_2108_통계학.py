import sys

N = int(sys.stdin.readline())
num = []
count = [0] * 8001

for i in range(N):
    n = int(sys.stdin.readline())
    num.append(n)
    count[n+4000] += 1
    
print(round(sum(num)/N))

print(sorted(num)[N//2])

mode = list(filter(lambda x: count[x] == max(count), range(len(count))))
if len(mode) == 1:
    print(mode[0]-4000)
else:
    print(mode[1]-4000)

print(max(num)-min(num))