def dfs(num):
    global cnt
    if num >= len(arg):
        cnt += 1
        return
    dfs(num * 2)
    arg[num] = cnt
    dfs(num * 2 + 1)

t = int(input())
for tc in range(1, t + 1):
    cnt = 0
    n = int(input())
    arg = [0 for _ in range(n + 1)]
    dfs(1)
    print(f'#{tc} {arg[1]} {arg[n//2]}')