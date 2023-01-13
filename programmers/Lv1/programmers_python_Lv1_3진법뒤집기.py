def solution(n):
    ternary = ''
    while n:
        ternary = str(n % 3) + ternary
        print(ternary)
        n = n // 3

    # answer = 0
    # for num in ternary[::-1]:
    #     answer = int(num) + answer * 3
    answer = sum([num*3**i for i, num in enumerate(map(int, ternary))])
    return answer

print(solution(45))