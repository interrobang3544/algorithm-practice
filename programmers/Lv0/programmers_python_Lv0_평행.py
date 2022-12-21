def solution(dots):
    answer = 0
    if gradient(dots[0], dots[1]) == gradient(dots[2], dots[3]) or gradient(dots[0], dots[2]) == gradient(dots[1], dots[3]) or gradient(dots[0], dots[3]) == gradient(dots[1], dots[2]):
        answer = 1
    return answer

def gradient(a, b):
    return (a[1]-b[1])/(a[0]-b[0])