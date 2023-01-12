def solution(price, money, count):
    answer = max(0, ((1+count)*price)/2*count - money)
    return answer