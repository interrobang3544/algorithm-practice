num_list = list(input().split())
sangsu_list = [int(num[::-1]) for num in num_list]

print(max(sangsu_list))