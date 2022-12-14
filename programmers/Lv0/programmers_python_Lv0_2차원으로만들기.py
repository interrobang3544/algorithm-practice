def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        temp = []
        for j in range(n):
            temp.append(num_list[i * n + j])
        answer.append(temp)
    return answer