def solution(s):
    num_list = list(map(int, s.split()))
    max_min_list = []
    max_min_list.append(str(min(num_list)))
    max_min_list.append(str(max(num_list)))
    return ' '.join(max_min_list)