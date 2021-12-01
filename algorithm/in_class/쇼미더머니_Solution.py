#5 3
#4 3 2 1 0
#0 1 2 3 4
#2 1 0 4 3
#1 2 3 4 0
#3 2 1 0 4

# 무대로 나갈 수 있는 위치 예시 여기선 4개
#(0, 0), (0, 4), (4, 0), (4, 4)
#합 50


# 상 하 좌 우 좌상대각 우상대각 좌하대각 우하대각
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(idx, lst):
    global max_cnt, N, M, P
    if len(lst) == M:
        cnt = 0
        for i in lst:
            y, x = i

            for j in range(8):
                ny = dy[j] + y
                nx = dx[j] + x
                if 0 <= ny < N and 0 <= nx < N:
                    cnt += 1
            cnt += MAP[y][x]
            if max_cnt < 50 + cnt:
                max_cnt = 50 + cnt
                print(lst)
        return

    if idx == P:
        return

    lst.append(STAGE[idx])
    dfs(idx + 1, lst)
    lst.pop()
    dfs(idx + 1, lst)



# N 관객석의 크기, M은 무대 이동 가능 횟수, P는 갈 수 있는 무대 갯수(전체 무대 수)
N, M, P = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0
for y in range(N):
    for x in range(N):
        max_cnt += MAP[y][x]

STAGE = []
for i in range(P):
    STAGE.append(list(map(int, input().split())))
visited = [0 for _ in range(P)]

dfs(0, [])

print(max_cnt)

