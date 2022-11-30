def solution(n):
    answer = 0
    length = len(str(n))
    for i in range(1, length + 1):
        print(i, length)
        m = n // 10 ** (length - i)
        n -= 10 ** (length - i) * m
        answer += m
    return answer