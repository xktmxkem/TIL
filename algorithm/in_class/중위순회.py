def dfs(n):
    global node
    if n > node:
        return


    dfs(2*n)
    ret.append(lst[n])
    dfs(2*n + 1)


for testcase in range(1, 11):
    node = int(input())
    lst = [0 for i in range(node + 1)]
    ret = []
    for i in range(1, node + 1):
        temp = list(input().split())

        lst[int(temp[0])] = temp[1]

    dfs(1)

    s = ''.join(ret)
    print('#{} {}'.format(testcase, s))