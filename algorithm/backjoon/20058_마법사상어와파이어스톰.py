#  맵의 크기 2 ** N x 2 ** N
# Q는 파이어스톰 쏘는 횟수
# L는 격자를 나누는 수 2 ** L씩 나눔
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
de = -1
def rotation(level):
    global N
    devide = 2 ** level
    maximum = 2 ** N
    NEW_MAP = [[0 for i in range(2**N)] for j in range(2 ** N)]
    x_start = 0
    x_end = devide
    y_start = 0
    y_end = devide
    while(1):
        if x_end > maximum:
            y_start += devide
            y_end += devide
            x_start = 0
            x_end = devide
            continue

        if y_end > maximum:
            break

        oy = y_start + devide - 1
        ox = x_start

        for y in range(y_start, y_end):
            oy = y_start + devide - 1
            for x in range(x_start, x_end):
                NEW_MAP[y][x] = MAP[oy][ox]
                oy -= 1
            ox += 1

        x_start += devide
        x_end += devide

    return NEW_MAP


def ice():
    global N
    border = 2**N
    lst = []
    for y in range(border):
        for x in range(border):
            cnt = 4
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x

                if 0 > ny or 0 > nx  or ny >= border or nx >= border or MAP[ny][nx] < 1:
                    cnt -= 1
                if cnt < 3:
                    lst.append([y, x])
                    break


    for i in lst:
        MAP[i[0]][i[1]] -= 1


def bfs(y,x):
    global N
    border = 2 ** N
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1
    cnt = 1
    while queue:
        ty, tx = queue.popleft()
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0 <= ny < border and 0 <= nx < border:
                if MAP[ny][nx] < 1:
                    continue
                if visited[ny][nx] == 1:
                    continue
                visited[ny][nx] = 1
                cnt += 1
                queue.append([ny, nx])

    return cnt



N, Q = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(2 ** N)]
# 쏠 때 마다 몇번째 단계로 쐇는지 계산
# 이때의 LEVEL을 바탕으로 격자를 계싼
LEVEL = list(map(int, input().split()))

for level in LEVEL:
    NEW_MAP = rotation(level)
    MAP = NEW_MAP
    ice()



total_ice = 0
ice_land =0
visited = [[0 for i in range(2 ** N)] for j in range(2**N)]
for y in range(2 ** N):
    for x in range(2 ** N):
        if MAP[y][x] > 0 :
            total_ice += MAP[y][x]
        if visited[y][x] == 0 and MAP[y][x] > 0:
            temp = bfs(y, x)
            ice_land = max(ice_land, temp)

print(total_ice)

if ice_land == 1:
    print(0)
else:
    print(ice_land)
