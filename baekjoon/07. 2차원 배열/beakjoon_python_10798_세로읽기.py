board = []
max_len = 0

for i in range(5):
    row = list(input())

    if len(row) > max_len:
        max_len = len(row)
        
    board.append(row)

for i in range(5):
    if max_len > len(board[i]):
        for _ in range(max_len - len(board[i])):
            board[i].append("-")

for j in range(max_len):
    for i in range(5):
        print(board[i][j] if board[i][j] != "-" else "", sep="", end="")