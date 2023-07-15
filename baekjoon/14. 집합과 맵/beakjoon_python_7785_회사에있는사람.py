import sys

n = int(sys.stdin.readline())
attendance = {}

for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter": attendance[name] = 1
    else: del attendance[name]

print(*sorted(attendance.keys(), reverse=True), sep="\n")