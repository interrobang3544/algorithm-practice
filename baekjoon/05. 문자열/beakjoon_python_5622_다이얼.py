word = input()
alphabet_dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for alphabet in word:
    for alphabet_dial_group in alphabet_dial_list:
        for alphabet_dial in alphabet_dial_group:
            if alphabet == alphabet_dial:
                time += 3 + alphabet_dial_list.index(alphabet_dial_group)
print(time)