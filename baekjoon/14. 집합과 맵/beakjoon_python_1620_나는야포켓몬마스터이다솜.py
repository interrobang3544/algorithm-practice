import sys
n, m = map(int, sys.stdin.readline().strip().split())

pokemon_dict = {}

for i in range(n):
  pokemon = sys.stdin.readline().strip()
  pokemon_dict[i + 1] = pokemon
  pokemon_dict[pokemon] = i + 1

for i in range(m):
  test = sys.stdin.readline().strip()
  if test.isdigit() == True:
    print(pokemon_dict[int(test)])
  elif test.isalpha() == True:
    print(pokemon_dict[test])