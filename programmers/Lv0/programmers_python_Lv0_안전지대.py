def solution(board):
    temp = [[0 for _ in range(len(board) + 2)] for _ in range(len(board) + 2)]
    for i in range(len(board)):
        for j in range(len(board)):
            temp[i+1][j+1] = board[i][j]

    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            check = 0
            for p in range(3):
                for q in range(3):
                    if temp[i+p][j+q] == 1:
                        check += 1
            if check == 0:
                answer += 1
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))