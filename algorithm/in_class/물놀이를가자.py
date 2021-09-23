from collections import deque
# 상, 하, 좌 , 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    global n
    global m
    cnt = 0
    cnt_min = []
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[y][x] = 1
    queue = deque()
    queue.append([y,x])
    while queue:
        cnt += 1
        now = queue.popleft()
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if ny >= n or nx >= m or ny < 0 or nx < 0:
                continue
            if visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            if board[ny][nx] == 'W':
                cnt_min.append(cnt)
                cnt = 0
                continue
            queue.append([ny,nx])
    print(cnt_min)
    return 0



t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    cnt_sum = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'L':
                cnt_sum += bfs(y, x)
    print(cnt_sum)
