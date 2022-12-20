sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def isPromising(i, j):
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
    
    for k in range(9):
        if sudoku[i][k] in candidate:
            candidate.remove(sudoku[i][k])
        if sudoku[k][j] in candidate:
            candidate.remove(sudoku[k][j])
            
    for p in range((i//3) * 3, (i//3) * 3 + 3):
        for q in range((j//3) * 3, (j//3) * 3 + 3):
            if sudoku[p][q] in candidate:
                candidate.remove(sudoku[p][q])
    
    return candidate

flag = False 
def doSudoku(x):
    global flag
    
    if flag: 
        return
        
    if x == len(zeros): 
        for row in sudoku:
            print(*row)
        flag = True 
        return
        
    else:    
        (i, j) = zeros[x]
        candidate = isPromising(i, j) #유망한 숫자들을 받음
        for num in candidate:
            sudoku[i][j] = num
            doSudoku(x + 1) 
            sudoku[i][j] = 0 
doSudoku(0)