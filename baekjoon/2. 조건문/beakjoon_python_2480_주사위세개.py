num1, num2, num3 = map(int, input().split())

if num1 == num2 == num3:
    prize = 10000 + num1 * 1000
elif num1 == num2:
    prize = 1000 + num1 * 100
elif num2 == num3:
    prize = 1000 + num2 * 100
elif num3 == num1:
    prize = 1000 + num3 * 100
else:
    prize = max(num1, num2, num3) * 100

print(prize)