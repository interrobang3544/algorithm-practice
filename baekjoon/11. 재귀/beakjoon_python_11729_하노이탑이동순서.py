def hanoi(n, s, e): #hanoi(n개의 원판, 시작 장대, 도착 장대)
    if n == 1 : #원판이 1개인 경우
        print(s, e)
        return
       
    hanoi(n - 1, s, 6 - s - e)   #n-1개의 원판 중간 장대로 이동
    print(s, e)                  #가장 큰 원판 도착 장대로 이동
    hanoi(n - 1, 6 - s - e, e)   #n-1개의 원판 도착 장대로 이동
    
N = int(input())
print(2**N - 1) #옮긴 횟수
hanoi(N, 1, 3) #수행 과정