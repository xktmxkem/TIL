from collections import deque
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global n
    global m
    global ans
    queue = deque()
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'W':
                queue.append([y, x, 0])
                visited[y][x] = 1
    while queue:
        now = queue.popleft()
        y, x, cnt = now[0], now[1], now[2]
        cnt += 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if ny >= n or nx >= m or ny < 0 or nx < 0:
                continue
            if visited[ny][nx] > 0:
                continue
            visited[ny][nx] = cnt
            ans += cnt
            queue.append([ny, nx, cnt])

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    visited = [[0 for i in range(m)] for j in range(n)]
    start = []
    ans = 0


    bfs()
    print(f'#{tc} {ans}')
