

def dfs(idx):
    global N
    # 오른쪽 끝까지 검사
    r_cnt = 0
    for n_right in range(idx + 1, N):
        if lst[idx] <= lst[n_right] : continue
        if visited[n_right][1] != -1:
            temp_cnt = visited[n_right][1]
        else:
            temp_cnt = dfs(n_right)
        r_cnt = max(r_cnt, temp_cnt)

    if r_cnt == 0:
        visited[idx][1] = 1
        return 1

    visited[idx][1] = r_cnt + 1
    return visited[idx][1]


def dfs2(idx):
    global N
    # 오른쪽 끝까지 검사
    l_cnt = 0
    for n_left in range(idx - 1, -1 , -1):
        if lst[idx] <= lst[n_left] : continue
        if visited[n_left][0] != -1:
            temp_cnt = visited[n_left][0]
        else:
            temp_cnt = dfs2(n_left)
        l_cnt = max(l_cnt, temp_cnt)

    if l_cnt == 0:
        visited[idx][0] = 1
        return 1

    visited[idx][0] = l_cnt + 1
    return visited[idx][0]






N = int(input())
lst = list(map(int, input().split()))
max_len = 0
cur_len = 0
visited = [[-1, -1] for _ in range(N)]

for i in range(len(lst)):
    if visited[i][1] == -1:
        dfs(i)
    if visited[i][0] == -1:
        dfs2(i)

max_cnt = 0
for i in visited:
    a = sum(i)
    if max_cnt < a:
        max_cnt = a

print(max_cnt - 1)
