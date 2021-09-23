def cal(oper, a, b):
    if oper == '+':
        return a+b
    if oper == '-':
        return a-b
    if oper == '/':
        return a/b
    if oper == '*':
        return a*b


def dfs(num):
    if num >= len(arg) or arg[num] == 'x':
        return

    if len(arg[num]) == 3:
        left = dfs(arg[num][1])
        right = dfs(arg[num][2])
        return cal(arg[num][0], left, right)
    else:
        return arg[num][0]



for tc in range(1, 11):
    n = int(input())
    arg = ['x' for _ in range(1001)]
    for i in range(n):
        tmp = list(input().split())
        if tmp[1].isdigit():
            arg[int(tmp[0])] = [int(tmp[1])]
        else:
            arg[int(tmp[0])] = [tmp[1], int(tmp[2]), int(tmp[3])]
    ans = dfs(1)
    print(f'#{tc} {int(ans)}')
