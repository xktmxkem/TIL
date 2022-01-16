import sys
sys.setrecursionlimit(10**6)
# 상, 하, 좌, 우, 좌상대각, 좌하대각, 우상대각, 우하대각
delta_y = [-1, 1, 0, 0, -1, 1, -1, 1]
delta_x = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(y, x):
    global w
    global h
    for i in range(8):
        ny = y + delta_y[i]
        nx = x + delta_x[i]
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue
        if MAP[ny][nx] == 0:
            continue
        if visited[ny][nx] == 1:
            continue
        visited[ny][nx] = 1
        bfs(ny, nx)
    return 1

while(1):
    # w : x, h : y
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        MAP = []
        for i in range(h):
            MAP.append(list(map(int, input().split())))

        visited = [[0 for i in range(w)] for j in range(h)]

        island = 0
        for y in range(h):
            for x in range(w):
                if MAP[y][x] != 0 and visited[y][x] == 0:
                    island += bfs(y,x)
        print(island)