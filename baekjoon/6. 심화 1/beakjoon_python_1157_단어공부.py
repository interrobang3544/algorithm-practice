word = input().upper()
alphabet = list(set(word))
count_list = [word.count(i) for i in alphabet]

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(alphabet[count_list.index(max(count_list))])