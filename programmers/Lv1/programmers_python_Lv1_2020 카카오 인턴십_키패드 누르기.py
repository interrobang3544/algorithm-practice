def findCoordinate(keynum):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*', 0, '#']]
    return [[i,j] for i in range(4) for j in range(3) if keypad[i][j]==keynum][0]

def calDistance(a, b):
    return sum([abs(findCoordinate(a)[i]-findCoordinate(b)[i]) for i in [0,1]])

def solution(numbers, hand):
    left_location = '*'
    right_location = '#'
    answer = ''
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_location = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right_location = num
        else:
            if calDistance(left_location, num) < calDistance(right_location, num):
                answer += 'L'
                left_location = num
            elif  calDistance(left_location, num) > calDistance(right_location, num):
                answer += 'R'
                right_location = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left_location = num
                elif hand == 'right':
                    answer += 'R'
                    right_location = num
    return answer