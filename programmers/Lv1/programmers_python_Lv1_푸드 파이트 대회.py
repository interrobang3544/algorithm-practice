def solution(food):
    answer = '0'
    for i, num in enumerate(food[:0:-1]):
        food_num = len(food)-i-1
        answer = str(food_num) * (num//2) + answer + str(food_num) * (num//2)
    return answer