for testcase in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for y in range(n):
        change = False
        for x in range(n):
            if table[x][y] == 1:
                change = True
            if table[x][y] == 2 and change:
                cnt += 1
                change = False

    print('#{} {}'.format(testcase, cnt))
