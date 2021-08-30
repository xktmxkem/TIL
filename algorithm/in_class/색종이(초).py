

board = [[0 for i in range(100)] for j in range(100)]
n = int(input())
paper = []
for i in range(n):
    y, x = map(int, input().split())
    for i in range(len(board) - y , len(board) - (y + 10), - 1):
        for j in range(x, x + 10):
            board[i][j] = 1

for i in board:
    print(i)
