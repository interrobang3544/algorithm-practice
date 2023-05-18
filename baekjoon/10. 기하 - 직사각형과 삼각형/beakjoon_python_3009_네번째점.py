x_list , y_list = [], []
for i in range(3):
  x, y = map(int, input().split())
  x_list.append(x)
  y_list.append(y)

x, y = 0, 0
for num in x_list:
  if x_list.count(num) == 1:
    x = num

for num in y_list:
  if y_list.count(num) == 1:
    y = num

print(x, y)