def dfs

n = int(input())

arg = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n):
    y, x = map(int, input().split())
    arg[y][x] = 1

dfs(1)