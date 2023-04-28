num = set(range(1, 10000))
remove_set = set()

for i in num:
    for n in str(i):
        i += int(n)
    remove_set.add(i)

self_numbers = num - remove_set

for j in sorted(self_numbers):
    print(j)