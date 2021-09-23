def dfs(num):
    global cnt
    if num == 0:
        return
    dfs(arg[num][0])
    dfs(arg[num][1])
    cnt += 1



t = int(input())
for tc in range(1, t + 1):
    e, n = map(int, input().split())
    info = list(map(int, input().split()))
    arg = [[0, 0] for _ in range(e + 2)]
    for i in range(0, len(info), 2):
        y, x = info[i : i + 2]
        if arg[y][0] == 0:
            arg[y][0] = x
        else:
            arg[y][1] = x
    cnt = 0
    dfs(n)
    print(f'#{tc} {cnt}')
