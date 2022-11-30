attendance_num= [i for i in range(1,31)]

for _ in range(28):
    n = int(input())
    attendance_num.remove(n)

print(attendance_num[0], attendance_num[1], sep='\n')