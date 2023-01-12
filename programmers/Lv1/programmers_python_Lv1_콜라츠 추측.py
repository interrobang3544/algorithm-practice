def solution(num):
    for i in range(500):
        if num == 1:
            answer = i
            return answer
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 +1
    answer = -1
    return answer