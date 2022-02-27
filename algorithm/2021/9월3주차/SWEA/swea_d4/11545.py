def is_garo(y, x):
    # 가로 범위 초과 확인
    global result
    if x + 3 > 3:
        return 0

    temp = arg[y][x]
    if temp == 'T':
        temp = arg[y][x + 1]
    for i in range(0, 4):
        if arg[y][x + i] == 'T':
            continue
        if temp != arg[y][x + i]:
            return 0
        if arg[y][x + i] == '.':
            return 0

    if arg[y][x] == 'T':
        result = arg[y][x + 1]
    else:
        result += arg[y][x]
    return result


def is_sero(y, x):
    # 세로 범위 초과 확인
    global result
    if y + 3 > 3:
        return 0

    temp = arg[y][x]
    if temp == 'T':
        temp = arg[y + 1][x]
    for i in range(0, 4):
        if arg[y + i][x] == 'T':
            continue
        if temp != arg[y + i][x]:
            return 0
        if arg[y + i][x] == '.':
            return 0

    if arg[y][x] == 'T':
        result = arg[y + 1][x]
    else:
        result += arg[y][x]
    return result


def is_daegak_left(y, x):
    #  범위 초과 확인
    global result
    if y + 3 > 3 or x + 3 > 3:
        return 0

    temp = arg[y][x]
    if temp == 'T':
        temp = arg[y + 1][x + 1]
    for i in range(0, 4):
        if arg[y + i][x + i] == 'T':
            continue
        if temp != arg[y + i][x + i]:
            return 0
        if arg[y + i][x + i] == '.':
            return 0

    if arg[y][x] == 'T':
        result = arg[y + 1][x + 1]
    else:
        result += arg[y][x]
    return result


def is_deagak_right(y, x):
    #  범위 초과 확인
    global result
    if y + 3 > 3 or x - 3 < 0:
        return 0

    temp = arg[y][x]
    if temp == 'T':
        temp = arg[y + 1][x - 1]
    for i in range(0, 4):
        if arg[y + i][x - i] == 'T':
            continue
        if temp != arg[y + i][x - i]:
            return 0
        if arg[y + i][x - i] == '.':
            return 0

    if arg[y][x] == 'T':
        result = arg[y + 1][x - 1]
    else:
        result += arg[y][x]
    return result


test = int(input())
for testcase in range(1, test + 1):
    arg = [input() for _ in range(4)]
    ignore = input()  # 무시함
    result = ''

    default = 'Draw'
    for y in range(4):
        for x in range(4):
            if arg[y][x] == '.':
                default = 'Game has not completed'
                continue
            if is_garo(y, x) or is_sero(y, x) or is_daegak_left(y, x) or is_deagak_right(y, x):
                break
        if result:
            break
    if result:
        print('#{} {} won'.format(testcase, result))
    else:
        print('#{} {}'.format(testcase, default))