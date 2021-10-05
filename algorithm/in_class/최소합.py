from collections import deque
dy = [1, 0]
dx = [0, 1]

# 그리드하지 못하다
# def bfs(y, x):
#     global n
#     queue = deque()
#     queue.append([y,x,0])
#     visited = [[0 for i in range(n)] for j in range(n)]
#     visited[0][0] = 1
#     while queue:
#         now = queue.popleft()
#         sum = now[2]
#         if now[0] == n - 1 and now[1] == n - 1:
#             ans.append(sum)
#         for i in range(2):
#             ny = dy[i] + now[0]
#             nx = dx[i] + now[1]
#
#             if 0 <= ny < n and 0 <= nx < n:
#                 sum += lst[ny][nx]
#                 queue.append([ny, nx, sum])

def dfs(y , x):
    global n
    if y >= n or x >= n : return 9999999999999
    if y == n-1 and x == n-1:
        return lst[y][x]

    a = dfs(y, x + 1)
    b = dfs(y + 1, x)
    return min(a,b) + lst[y][x]




t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    ans = dfs(0, 0)
    print(f'#{tc} {ans}')