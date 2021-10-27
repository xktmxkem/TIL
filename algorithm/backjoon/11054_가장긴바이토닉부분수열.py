

def dfs(idx):
    global N

    l_cnt = 0
    r_cnt = 0




N = int(input())
lst = list(map(int, input().split()))
max_len = 0
cur_len = 0
visited = [[-1, -1] for _ in range(N)]

for i in range(len(lst)):
    dfs(i)

print(visited)
print(max_len)