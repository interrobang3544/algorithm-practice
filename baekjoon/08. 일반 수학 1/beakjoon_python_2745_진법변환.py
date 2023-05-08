num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
answer = 0
for i, num in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.index(num)
print(answer)

# 더 쉬운 방법
# a, b = input().split()
# print(int(a, int(b)))
