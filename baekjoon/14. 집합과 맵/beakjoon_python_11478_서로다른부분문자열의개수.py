s = input()
part_set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        part_set.add(s[i:j+1])

print(len(part_set))