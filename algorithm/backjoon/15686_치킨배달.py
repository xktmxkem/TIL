# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
#
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
#
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

#첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

# M개 치킨집이 최대 갯수이므로 나머지는 폐업 해야함

from collections import deque
import copy
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 최소거리 찾는 알고리즘
def bfs(lst):
    global N, M, HOUSE, MIN_DISTANCE
    house_cnt = 0
    house_distance = 0
    queue = deque()
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in lst:
        y, x = i[0], i[1]
        visited[y][x] = 1
        queue.append([y, x, 1])


    while queue:
        now = queue.popleft()
        y = now[0]
        x = now[1]
        distance = now[2]
        if house_distance >= MIN_DISTANCE:
            break
        if house_cnt == HOUSE:
            MIN_DISTANCE = house_distance
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if visited[ny][nx] > 0:
                continue
            visited[ny][nx] = distance

            if MAP[ny][nx] == 1:
                house_cnt += 1
                house_distance += distance


            queue.append([ny, nx, distance + 1])

# 치킨집 M개 만큼 뽑기
def dfs(idx, lst, level):
    global M
    if len(lst) == M:
        temp = copy.deepcopy(lst)
        CHICKEN_CASE.append(temp)
        return

    if idx >= len(CHICKEN):
        return

    lst.append(CHICKEN[idx])
    dfs(idx + 1, lst, level + 1)
    lst.pop()
    dfs(idx + 1, lst, level + 1)



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
CHICKEN = []
HOUSE = 0
CHICKEN_CASE = []
MIN_DISTANCE = int(21e8)
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 2:
            CHICKEN.append([y, x])
        if MAP[y][x] == 1:
            HOUSE += 1

dfs(0, [], 1)
for i in CHICKEN_CASE:
    bfs(i)

print(MIN_DISTANCE)
