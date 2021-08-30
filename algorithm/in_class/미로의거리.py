from collections import deque

def bfs(y, x, min_path):
    global n

    queue = deque()
    queue.append([y, x, min_path])
    # 위 아래 좌 우
    dy = [-1, 1, 0, 0]
    dx = [ 0, 0, -1, 1]

    while(len(queue) > 0):
        now = queue.popleft()


        for t in range(4):
            ny = now[0] + dy[t]
            nx = now[1] + dx[t]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if arg[ny][nx] == '1':
                continue

            if visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1

            if arg[ny][nx] == '3':
                return now[2]

            queue.append([ny, nx, now[2] + 1])

    return 0
T = int(input())
for testcase in range(1, T + 1):
    n = int(input())
    arg = [input() for j in range(n)]
    visited = [[0 for i in range(n)] for j in range(n)]
    min_path = 0
    for y in range(n):
        for x in range(n):
            if arg[y][x] == '2':
                min_path = bfs(y, x, min_path)

    print('#{} {}'.format(testcase, min_path))