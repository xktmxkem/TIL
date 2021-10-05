from collections import deque
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    global n, m, answer
    answer += 1
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        now = queue.popleft()
        ty, tx = now[0], now[1]
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny >= n or nx >= m or ny < 0 or nx < 0:
                continue
            if board[ny][nx] == 0:
                continue
            if visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            queue.append([ny, nx])
    return

def dfs(now):


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for i in range(m)] for j in range(n)]
    answer = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 2 and visited[y][x] == 0:
                bfs(y, x)
    print(f'#{tc} {answer}')