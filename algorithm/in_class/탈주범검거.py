from collections import deque
def pipe(num):
    # 상하좌우
    if num == 1:
        ny = [-1, 1, 0, 0]
        nx = [0, 0, -1, 1]
    # 상하
    elif num == 2:
        ny = [-1, 1]
        nx = [0, 0]
    # 좌우
    elif num == 3:
        ny = [0, 0]
        nx = [-1, 1]
    # 상우
    elif num == 4:
        ny = [-1, 0]
        nx = [0, 1]
    # 하우
    elif num == 5:
        ny = [1, 0]
        nx = [0, 1]
    # 하좌
    elif num == 6:
        ny = [1, 0]
        nx = [0, -1]
    # 상좌
    elif num == 7:
        ny = [-1, 0]
        nx = [0, -1]
    return [ny, nx]

def check(ny, nx, next):
    # 상
    if ny == -1 and nx == 0:
        if next == 3 or next == 4 or next == 7:
            return 0
        else:
            return 1
    # 하
    if ny == 1 and nx == 0:
        if next == 3 or next == 5 or next == 6:
            return 0
        else:
            return 1
    # 좌
    if ny == 0 and nx == -1:
        if next == 2 or next == 6 or next == 7:
            return 0
        else:
            return 1
    # 우
    if ny == 0 and nx == 1:
        if next == 2 or next == 4 or next == 5:
            return 0
        else:
            return 1
def bfs():
    global n, m, r, c, l, ans
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[r][c] = 1
    queue = deque()
    queue.append([r, c, 1])
    while queue:
        now = queue.popleft()
        y, x, time = now[0], now[1], now[2]
        if time >= l:
            continue
        time += 1
        temp = pipe(board[y][x])
        ny, nx = temp[0], temp[1]
        for i in range(len(ny)):
            dy = ny[i] + y
            dx = nx[i] + x
            if dy >= n or dx >= m or dy < 0 or dx < 0:
                continue
            if board[dy][dx] == 0:
                continue
            if check(ny[i], nx[i], board[dy][dx]) == 0:
                continue
            if visited[dy][dx] > 0:
                continue
            visited[dy][dx] = time

            ans += 1
            queue.append([dy, dx, time])

t = int(input())
for tc in range(1, t + 1):
    # 세로 : n, 가로 : m, 맨홀 위치 세로 : r, 맨홀 위치 가로 : c, 탈출 후 시간 : l
    n, m, r, c, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 1
    bfs()
    print(f'#{tc} {ans}')