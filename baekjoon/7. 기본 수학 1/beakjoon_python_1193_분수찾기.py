X = int(input())
total = 0
start_num = 0

while X > total:
    start_num += 1
    total += start_num

dif = total - X
a = 1 + dif
b = start_num - dif

if start_num % 2 == 1:
    print(f'{a}/{b}') 
else:
    print(f'{b}/{a}')