# -1 : 검은색 블록, 0 : 무지개 블록. M(이하의 숫자) : 일반블록
# 검은색은 들어가면 안됨
# 무지개는 아무 상관없음
# 일반 블록은 적어도 하나 있어야 하며 색이 모두 같아야함
# 그룹에 속한 블록의 갯수는 최소 2개
# 기준 블록은 무지개 아닌 블록중 세로가 가장 작고 여러개라면 가로가 가장 작은 블록
# 크기가 가장 큰 블록 찾는다. 그룹이 여러개라면 무지개 블록이 가장 많은 블록, 이 후에는 기준 블록이 행이 가장 큰 것을, 그것도 여러개면
# 열이 가장 큰 것을
# 1에서 찾은 블록 그룹의 모든 블록을 제거, 블록의 수를 B라고 했을 떄 B^2 점을 획득
# 격자에는 중력
# 격자는 반시계로 회전
# 다시 격자에 중력 작용
# 중력 작용시 검은 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동, 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속됨
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    global N
    queue = deque()
    queue.append([y, x])
    start = MAP[y][x]
    visited[y][x] = 1
    rainbow = []
    lst = [[y,x]]
    cnt = 1
    while queue:
        now = queue.popleft()
        ty = now[0]
        tx = now[1]
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                # 검은색이면 돌아가기
                if MAP[ny][nx] == -1: continue
                # 빈공간이면 돌아가기
                if MAP[ny][nx] == -2: continue
                # 시작 점과 다른 값이고 무지개 블록이 아니라면 돌아가기
                if MAP[ny][nx] != start and MAP[ny][nx] != 0: continue
                # 방문한 블록이라면 돌아가기
                if visited[ny][nx] == 1:continue
                visited[ny][nx] = 1
                # 무지개 블록이라면 초기화를 위해 0으로
                if MAP[ny][nx] == 0:
                    rainbow.append([ny, nx])
                # 갯수 1추가
                cnt += 1
                # 탐색
                lst.append([ny, nx])
                queue.append([ny, nx])
    # 무지개는 다시 0으로
    for i in rainbow:
        vy, vx = i[0], i[1]
        visited[vy][vx] = 0
    lst.append([cnt, len(rainbow), y, x])
    return lst

def gravity():
    global N
    for y in range(N - 2, -1 , -1):
        for x in range(N - 1, -1 ,-1):
            if MAP[y][x] != -1 and MAP[y][x] != -2:
                by = y
                ny = y + 1
                # 마지막 인덱스 값만 찾아서 바꾸기
                while(1):
                    if ny >= N : break
                    if MAP[ny][x] == -1 or MAP[ny][x] != -2: break
                    MAP[ny][x], MAP[by][x] = MAP[by][x], MAP[ny][x]
                    by = ny
                    ny += 1

def turn():
    global N
    return_lst = [[] for _ in range(N)]
    idx = 0
    for x in range(N -1, -1 , -1):
        for y in range(N):
            return_lst[idx].append(MAP[y][x])
        idx += 1

    return return_lst


# 한변의 크기 N, 색상의 개수 M
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

final_score = 0
while(1):
    visited = [[0 for i in range(N)] for j in range(N)]
    max_cnt = 0
    max_lst = []
    for y in range(N):
        for x in range(N):
            if MAP[y][x] > 0 and visited[y][x] != 1:
                temp_lst = bfs(y, x)
                # [-1][0] : 블록수 / [-1][1] : 무지개 블록 수 / [-1][2] : 기준블록 y/ [-1][3] : 기준블록 x
                cnt = temp_lst[-1][0]
                if cnt == max_cnt:
                    # 무지개 블록 수 비교
                    if max_lst[-1][1] <= temp_lst[-1][1]:
                        max_cnt = cnt
                        max_lst = temp_lst
                    # 필요 없는 부분
                    # elif max_lst[-1][1] == temp_lst[-1][1]:
                    #     # 행 비교
                    #     if max_lst[-1][2] < temp_lst[-1][2]:
                    #         max_cnt = cnt
                    #         max_lst = temp_lst
                    #         # 열 비교
                    #     elif max_lst[-1][2] == temp_lst[-1][2]:
                    #         if max_lst[-1][3] < temp_lst[-1][3]:
                    #             max_cnt = cnt
                    #             max_lst = temp_lst

                elif max_cnt < cnt:
                    max_cnt = cnt
                    max_lst = temp_lst

    if max_cnt < 2:
        break
    final_score += (max_cnt ** 2)

    for i in max_lst[:len(max_lst) - 1]:
        gy, gx = i[0], i[1]
        MAP[gy][gx] = -2

    gravity()
    MAP = turn()
    gravity()

print(final_score)
