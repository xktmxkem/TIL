from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(y, x, goal):
    global h, w, n, total_time
    visited = [[0 for i in range(w)] for j in range(h)]
    queue = deque()
    queue.append([y, x, 0])
    visited[y][x] = 1
    while queue:
        now = queue.popleft()
        ty, tx, time = now[0], now[1], now[2]
        time += 1
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny >= h or nx >= w or ny < 0 or nx < 0:
                continue
            if board[ny][nx] == '#':
                continue
            if visited[ny][nx] > 0:
                continue
            visited[ny][nx] = time

            if board[ny][nx] == str(goal):
                total_time += time
                if goal != len(goal_lst):
                    position.append([ny, nx])
                    return
                else:
                    return
            queue.append([ny, nx, time])



t = int(input())
for tc in range(1, t + 1):
    # h 세로 w 가로 n 배달지역수
    total_time = 0
    h, w, n = map(int, input().split())
    goal_lst = [i for i in range(1, n + 1)]
    board = [input() for _ in range(h)]
    position = deque()
    position.append([0, 0])

    i = 0
    while position:
        temp = position.popleft()
        bfs(temp[0], temp[1], goal_lst[i])
        i += 1

    print(f'#{tc} {total_time}')
