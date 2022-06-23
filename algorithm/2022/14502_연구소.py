# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
#
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
#
# 빈 칸의 개수는 3개 이상이다.
#
# 벽은 무조건 3개
# 바이러스의 갯수는 2 <= 바이러스 <= 10
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
import copy
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs():
    global N, M, TOTAL_EMPTY
    queue = deque(TOTAL_VIRUS)
    TEST_MAP = copy.deepcopy(MAP)

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < N and 0 <= nx < M:
                if TEST_MAP[ny][nx] == 1 or TEST_MAP[ny][nx] == 2:
                    continue
                TEST_MAP[ny][nx] = 2
                queue.append([ny, nx])
    cnt = 0
    for i in range(N):
        cnt += TEST_MAP[i].count(0)
    TOTAL_EMPTY = max(cnt, TOTAL_EMPTY)


def wall(wall_cnt):
    global N, M
    if wall_cnt == 3:
        bfs()
        return
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 0:
                MAP[y][x] = 1
                wall(wall_cnt + 1)
                MAP[y][x] = 0



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
TOTAL_VIRUS = []
TOTAL_EMPTY = 0

for y in range(N):
    for x in range(M):
        if MAP[y][x] == 2:
            TOTAL_VIRUS.append([y, x])
wall(0)
print(TOTAL_EMPTY)