from collections import deque
# N X N 땅크기
# L이상 R 이하면 국경열어 같은 땅이라 인식
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(y, x):
    global N, L, R
    queue = deque()
    queue.append([y, x])
    visited = [[0 for i in range(N)] for j in range(N)]
    visited[y][x] = 1
    cnt = MAP[y][x]
    ans = [[y, x]]
    while queue:
        now = queue.popleft()
        ty, tx = now[0], now[1]
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if abs(MAP[ty][tx] - MAP[ny][nx]) < L or abs(MAP[ty][tx] - MAP[ny][nx]) > R: continue

                if visited[ny][nx] == 1: continue
                visited[ny][nx] = 1

                cnt += MAP[ny][nx]
                ans.append([ny, nx])
                queue.append([ny, nx])

    avg = int(cnt // len(ans))
    for i in ans:
        y, x = i
        MAP[y][x] = avg



N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 0
x_idx = 0
y_idx = 0
flag = True
while flag == True :
    check = 0
    while y_idx < N:
        while x_idx < N:
            for i in range(4):
                ny = y_idx + dy[i]
                nx = x_idx + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if  L <= abs(MAP[y_idx][x_idx] - MAP[ny][nx]) <= R:
                        bfs(y_idx, x_idx)
                        check += 1
            x_idx += 1
        y_idx += 1
    if check:
        ans += 1
    else:
        flag = False
for i in MAP:
    print(i)

print(ans)