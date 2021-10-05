from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def blossom(y, x):
    global sero, garo
    queue = deque()
    queue.append([y, x, 0])
    visited = [[0 for i in range(garo)] for j in range(sero)]
    visited[y][x] = 1
    max_cnt = 0
    while queue:
        now = queue.popleft()
        cnt = now[2]
        if cnt > max_cnt:
            max_cnt = cnt
        cnt += 1
        for i in range(4):
            ny = dy[i] + now[0]
            nx = dx[i] + now[1]
            if ny < 0 or nx < 0 or ny >= sero or nx >= garo: continue

            if MAP[ny][nx] == 'W': continue

            if visited[ny][nx] > 0: continue
            visited[ny][nx] = cnt


            queue.append([ny, nx, cnt])

    ans.append(max_cnt)




sero, garo = map(int, input().split())
MAP = [input() for _ in range(sero)]
ans = []

for y in range(sero):
    for x in range(garo):
        if MAP[y][x] == 'L':
            blossom(y, x)
print(max(ans))

