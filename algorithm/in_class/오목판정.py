# 좌 하 좌에서우대각 우에서좌대각
dy = [0, 1, 1, 1]
dx = [1, 0, 1, -1]

def check(y, x):
    i = 0
    while(i < 4):
        ny = y
        nx = x
        for j in range(4):
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                i += 1
                break
            if board[ny][nx] == '.':
                i += 1
                break
        else:
            return 1
    return 0

T = int(input())
for testcase in range(1, T + 1):
    n = int(input())
    board = [input() for _ in range(n)]
    ret = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == 'o':
                ret = check(y, x)
            if ret:
                break
        if ret:
            break
    if ret:
        print('#{} YES'.format(testcase))
    else:
        print('#{} NO'.format(testcase))