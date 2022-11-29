def solution(order):
    order_list = list(str(order))
    answer = order_list.count('3') + order_list.count('6') + order_list.count('9')
    return answer

solution(36969122)