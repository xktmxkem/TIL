color = ['W', 'B', 'R']

def dfs(level):
    global n
    global cnt
    # 제일 최근


    if level == n - 1:
        if temp[-1] != 'R':
            return
        s = ''.join(temp)
        ret.append(s)

        return

    for i in range(3):
        if temp[-1] == 'W' and color[i] == 'R':
            continue
        if temp[-1] == 'B' and color[i] == 'W':
            continue
        if temp[-1] == 'R' and color[i] != 'R':
            continue
        temp.append(color[i])
        dfs(level + 1)
        temp.pop()

# W B R 순으로
T = int(input())
for testcase in range(1, T + 1):
    # n : y , m : x
    n, m = map(int, input().split())
    s = ''

    temp = [] # dfs 내부에서 돌아갈 리스트
    ret = [] # 최종 가능한 경우수 부분집합 받아옴
    flag = [input() for _ in range(n)]
    temp.append(color[0])
    dfs(0)


    min_sum = 10**21
    for i in range(len(ret)):
        cnt = 0
        for y in range(n):
            for x in range(m):
                if flag[y][x] != ret[i][y]:
                    cnt += 1
        if min_sum > cnt:
            min_sum = cnt
    print('#{} {}'.format(testcase, min_sum))