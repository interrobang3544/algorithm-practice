def solution(d, budget):
    answer = 0
    for team_budget in sorted(d):
        budget -= team_budget
        if budget < 0:
            break
        answer += 1
    return answer