S = input()

ans = []
for i in range(97, 123):
    a_to_z = chr(i)
    try:
        print(S.index(a_to_z), end=' ')
    except:
        print(-1, end=' ')