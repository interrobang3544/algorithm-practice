def solution(lines):
    temp = [0 for _ in range(0, 200)]
    for i in range(len(lines)):
        for num in range(lines[i][0], lines[i][1]):
            temp[num + 100] += 1
    answer = len(list(filter(lambda x: x > 1, temp)))
    return answer
