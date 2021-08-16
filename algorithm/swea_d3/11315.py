def is_garo(y, x):

    if x + 5 - 1 >= n:
        return 0

    for i in range(5):
        if board[y][x + i] != 'o':
            return 0
    return 1


def is_sero(y, x):
    # 초과하는지 검사
    if y + 5 - 1 >= n:
        return 0

    for i in range(5):
        if board[y + i][x] != 'o':
            return 0
    return 1


def is_daegak_leftToright(y, x):
    if x + 5 - 1 >= n or y + 5 - 1 >= n:
        return 0

    for i in range(5):
        if board[y + i][x + i] != 'o':
            return 0
    return 1

def is_daegak_rightTOleft(y, x):
    if x + 5 - 1 >= n or y - 5 + 1 < 0:
        return 0

    for i in range(5):
        if board[y - i][x + i] != 'o':
            return 0
    return 1



test = int(input())
for test in range(1, test + 1):

    n = int(input())
    board = [input() for _ in  range(n)]
    #셋 중에 하나라도 만족한다면 1 이상이 되도록 설계
    result = 0

    for y in range(n):
        for x in range(n):
            result += is_sero(y,x) + is_garo(y,x) + is_daegak_leftToright(y, x) + is_daegak_rightTOleft(y, x)


    if result > 0:
        print('#{} YES'.format(test))
    else:
        print('#{} NO'.format(test))

