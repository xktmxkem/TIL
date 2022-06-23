
# y, x
FIRST = [
    [[0, 1]],
    [[1, 0]],
    [[-1, 0]],
    [[0, -1]]
]
SECOND = [
    [[0, 1], [0, -1]],
    [[-1, 0], [1, 0]],
]
THIRD = [
    [[0, 1], [-1, 0]],
    [[0, -1], [-1, 0]],
    [[0, -1], [1, 0]],
    [[0, 1], [1, 0]],
]
FOURTH = [
    [[0, 1], [-1, 0], [0, -1]],
    [[0, -1], [-1, 0], [1, 0]],
    [[0, -1], [1, 0], [0, 1]],
    [[0, 1], [1, 0], [-1, 0]],
]
FIFTH = [
    [[0, 1], [0, -1], [1, 0], [-1, 0]]
]

def dfs(camera_cnt, area_cnt):

    global camera, N, M, area, min_area
    if camera_cnt == len(camera):
        if area_cnt < min_area:
            min_area = area_cnt
        return
    # MAP[y][x] y x
    now_camera = camera[camera_cnt]
    now_y = camera[camera_cnt][1]
    now_x = camera[camera_cnt][2]
    if now_camera[0] == 1:
        now_array = FIRST
    elif now_camera[0] == 2:
        now_array = SECOND
    elif now_camera[0] == 3:
        now_array = THIRD
    elif now_camera[0] == 4:
        now_array = FOURTH
    else:
        now_array = FIFTH

    for array in now_array:
        check_area = 0
        changes = []
        for pos in array:
            ny = now_y
            nx = now_x
            while 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] == 0:
                    check_area += 1
                    MAP[ny][nx] = -1
                    changes.append([ny, nx])
                elif MAP[ny][nx] == 6:
                    break
                ny += pos[0]
                nx += pos[1]
        dfs(camera_cnt + 1, area_cnt - check_area)
        for change in changes:
            ty = change[0]
            tx = change[1]
            MAP[ty][tx] = 0


N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

camera = []
area = 0
min_area = int(21e8)
for y in range(N):
    for x in range(M):
        if MAP[y][x] % 6 != 0:
            camera.append([MAP[y][x], y, x])
        elif MAP[y][x] == 0:
            area += 1
dfs(0, area)
print(min_area)