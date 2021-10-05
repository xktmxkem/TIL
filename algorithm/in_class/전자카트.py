def dfs(now, level, cost):
    global N
    if level == N - 1:
        ans.append(cost)
    for next in range(N):
        if visited[next] == 1:
            continue
        visited[next] = 1
        dfs(next, level + 1, cost + MAP[now][next])

t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    visited[0] = 1
    ans = []