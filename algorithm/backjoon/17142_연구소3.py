import copy
from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(select_cnt, idx):
    global M
    if select_cnt == M:
        temp = copy.deepcopy(TEMP_SELECT_VIRUS)
        FINAL_SELECT_VIRUS.append(temp)
        return
    if idx >= len(VIRUS):
        return
    TEMP_SELECT_VIRUS.append(VIRUS[idx])
    dfs(select_cnt + 1, idx + 1)
    TEMP_SELECT_VIRUS.pop()
    dfs(select_cnt, idx + 1)

def bfs(CASE):
    global N, M
    queue = deque()
    visited = [[0 for i in range(N)] for j in range(N)]
    MIN_TIME = 0
    for pos in CASE:
        visited[pos[0]][pos[1]] = 1
        queue.append([pos[0], pos[1], 1])

    for pos2 in WALL:
        visited[pos[0]][pos[1]] = -1

    while queue:
        virus = queue.popleft()
        y = virus[0]
        x = virus[1]
        time = virus[2]
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < N and 0 <= nx < N:
                if MAP[ny][nx] == 1:
                    continue
                if visited[ny][nx] > 0:
                    continue
                visited[ny][nx] = time

                if time > MIN_TIME and MAP[ny][nx] != 2:
                    MIN_TIME = time
                queue.append([ny, nx, time + 1])

    for ay in range(N):
        for ax in range(N):
            if visited[ay][ax] == 0 and MAP[ay][ax] == 0:
                return


    MIN_TIME_CASE.append(MIN_TIME)

# 연구소 크기 N, 바이러스 개수 M

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
VIRUS = []
WALL = []
TEMP_SELECT_VIRUS = []
FINAL_SELECT_VIRUS = []
MIN_TIME_CASE = []
EMPTY = 0
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 2:
            VIRUS.append([y, x])
        if MAP[y][x] == 1:
            WALL.append([y, x])
        if MAP[y][x] == 0:
            EMPTY += 1
if EMPTY:
    dfs(0, 0)
    for CASE in FINAL_SELECT_VIRUS:
        bfs(CASE)
    if MIN_TIME_CASE:
        print(min(MIN_TIME_CASE))
    else:
        print(-1)
else:
    print(0)