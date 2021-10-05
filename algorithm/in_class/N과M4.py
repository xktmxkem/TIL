# 중복조합

def dfs(level, start):
    global n, m
    if level == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    #선택 후 재귀호출
    for i in range(start, n + 1):
        lst.append(i)
        dfs(level + 1, i)
        lst.pop()

n, m = map(int, input().split())
lst = []
dfs(0, 1)