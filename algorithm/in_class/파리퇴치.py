from collections import deque
# 아래로 오른쪽
dy = [1, 0]
dx = [0, 1]

def bfs(y,x):
    global n
    global m
    cnt = board[y][x]
    size_x = x + (m - 1)
    size_y = y + (m - 1)
    queue = deque()
    queue.append([y,x])
    visitied = [[0 for i in range(n)] for j in range(n)]
    while(len(queue) > 0):
        now = queue.pop()
        for i in range(2):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]

            # 맵 사이즈 넘어가면 continue
            if ny >= n or nx >= n or nx < 0 or ny < 0: continue
            # 파리채 사이즈 넘어가면 continue
            if ny > size_y or nx > size_x : continue
            # 방문한 곳이라면 continue
            if visitied[ny][nx] == 1: continue
            visitied[ny][nx] = 1
            # 다 아니라면 큐에 추가
            queue.append([ny, nx])
            cnt += board[ny][nx]
    return cnt

T = int(input())

for testcase in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_num = board[0][0]
    for y in range(n):
        for x in range(n):

            ret = bfs(y, x)
            if max_num < ret:
                max_num = ret

    print("#{} {}".format(testcase, max_num))
