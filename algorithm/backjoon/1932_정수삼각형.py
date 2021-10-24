from collections import deque
def dfs(level, idx, cnt):
    global N

    if cnt <= lst[level][idx]:
        return
    lst[level][idx] = cnt

    if level + 1 == N:
        return

    if 0 <= idx + 1 < len(triangle[level + 1]):
        dfs(level + 1, idx + 1, cnt + triangle[level + 1][idx + 1])

    if 0 <= idx < len(triangle[level + 1]):
        dfs(level + 1, idx , cnt + triangle[level + 1][idx])

    return

def bfs(y, x):
    global N
    queue = deque()
    queue.append([y, x, triangle[y][x]])
    lst[y][x] = triangle[y][x]
    cnt = 0
    while queue:
        now = queue.popleft()
        level = now[0]
        idx = now[1]
        cnt = now[2]

        for i in range(2):
            n_idx = idx + i
            if level + 1 == N : continue
            if n_idx >= len(triangle[level + 1]) : continue
            if cnt + triangle[level + 1][n_idx] < lst[level + 1][n_idx]: continue
            lst[level + 1][n_idx] = cnt + triangle[level + 1][n_idx]
            queue.append([level + 1, n_idx, cnt + triangle[level + 1][n_idx]])






N = int(input())
triangle =[list(map(int, input().split())) for i in range(N)]
lst = []
for i in range(1, N + 1):
    lst.append([0] * i)

bfs(0, 0)

print(max(lst[N-1]))