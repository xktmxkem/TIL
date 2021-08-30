def dfs(n):
    if n == 0:
        return
    result.append(n)
    dfs(tree[2*n])
    dfs(tree[2*n + 1])


T = int(input())
for testcase in range(1, T + 1):
    tree = [0 for _ in range (200)]
    n = int(input())
    tree[1] = 1
    for i in range(n - 1):
        now, next = map(int, input().split())
        if tree[now * 2] == 0:
            tree[now * 2] = next
        else:
            tree[(now * 2) + 1] = next
    result = []
    dfs(1)
    s = ' '.join(map(str, result))
    print('#{} {}'.format(testcase, s))