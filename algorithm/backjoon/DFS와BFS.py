def dfs(now):
    ans.append(now)
    if now == n:
        return

    for next in range(n + 1):
        if visited_dfs[next] == 1:
            continue
        visited_dfs[next] = 1
        if near_array[now][next] == 1:
            dfs(next)
    pass

def bfs(v):
    pass


n, m, v = map(int, input().split())

near_array = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(m):
    y, x = map(int, input().split())
    near_array[y][x] = 1

visited_dfs = [0 for i in range(n + 1)]
visited_dfs[0] = 1
ans = []
dfs(v)
print(ans)