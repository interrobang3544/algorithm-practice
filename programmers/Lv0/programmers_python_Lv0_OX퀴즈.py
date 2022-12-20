def solution(quiz):
    answer = []
    for fomula in quiz:
        part = fomula.split(' ')
        if cal(*part[0:3]) == int(part[4]):
            answer.["O"]
        else:
            answer.["X"]
    return answer

def cal(n, operator, m):
    if operator = "+":
        return int(n) + int(m)
    elif operator = "-":
        return int(n) - int(m)
        
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
