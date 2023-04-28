N = int(input())
origin = list(map(int, input().split()))
new = []

for i in range(N):
    new.append(origin[i]/max(origin)*100)

print(sum(new)/len(new))