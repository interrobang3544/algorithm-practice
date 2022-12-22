def solution(phone_number):
    answer = phone_number[-4:].rjust(len(phone_number), "*")
    return answer