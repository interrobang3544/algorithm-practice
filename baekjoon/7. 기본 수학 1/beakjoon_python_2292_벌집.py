N = int(input())
room = 1
num = 1

while N > room:
    room += 6 * num
    num += 1

print(num)