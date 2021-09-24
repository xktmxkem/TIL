


from collections import deque

def start():
    qu.append((7, 0,0))
    visited[7][0] = 1
    qu.append((6, 0,0))
    visited[6][0] = 1
    qu.append((5, 0,0))
    visited[5][0] = 1
    qu.append((6, 1,0))
    visited[6][1] = 1
    qu.append((7, 1,0))
    visited[7][1] = 1
    qu.append((7, 2,0))
    visited[7][2] = 1

MAP = [
"______###",
"______###",
"______###",
"_____####",
"____##___",
"#________",
"##_______",
"###______"
]

visited = [[0 for _ in range (9)] for _ in range(8)]
qu = deque()
# 시작지점을 등록하기 (큐 두개 마련해서 등록해도 됨)
start()
# bfs 돌려서 두 지점 사이 거리구하기

dy = [-1,1,0,0]
dx = [0,0,-1,1]
ans = 0
while qu :
    y,x,level= qu.popleft()
    if MAP[y][x] == '#' and level != 0:
        ans = level - 1
        break
    for t in range(4):
        ny = y + dy[t]
        nx = x + dx[t]
        if ny < 0 or nx < 0 or ny >= 8 or nx >= 9 : continue
        if visited[ny][nx] == 1 : continue
        visited[ny][nx] = 1
        qu.append((ny,nx, level + 1))

print(ans)