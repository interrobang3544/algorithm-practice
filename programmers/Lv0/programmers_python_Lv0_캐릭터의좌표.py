def solution(keyinput, board):
    direction = {'left':(-1,0),
                'right':(1,0),
                'up':(0,1),
                'down':(0,-1)
                }
    answer = [0, 0]
    
    for key in keyinput:
        dx, dy = direction[key]
        if abs(answer[0] + dx) > board[0]//2 or abs(answer[1] + dy) > board[1]//2:
            continue
        else:
            answer[0] += dx
            answer[1] += dy

    return answer

solution(["left", "right", "up", "right", "right"], [11, 11])