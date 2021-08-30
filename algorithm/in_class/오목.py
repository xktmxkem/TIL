def is_garo(y,x):
    # 현재 돌의 색상
    color = board[y][x]
    # 범위 넘을때
    if x + 4 >= 19: return 0
    # 다른 값이 나올때
    for i in range(5):
        if board[y][x + i] != color : return 0
    # 6목일때
    # 제일 앞줄 6목 체크
    if x - 1 < 0:
        if board[y][x + 5] == color: return 0
    # 제일 뒷줄 6목 체크
    elif x + 4 == 18:
        if board[y][x - 1] == color : return 0
    # 가운데 6목체크
    else:
        if board[y][x + 5] == color or board[y][x - 1] == color : return 0

    return 1

def is_sero(y,x):
    # 현재 돌의 색상
    color = board[y][x]
    # 범위 넘을때
    if y + 4 >= 19: return 0
    # 다른 값이 나올때
    for i in range(5):
        if board[y + i][x] != color : return 0
    # 6목일때
    # 제일 앞줄 6목 체크
    if y - 1 < 0:
        if board[y + 5][x] == color: return 0
    # 제일 뒷줄 6목 체크
    elif y + 4 == 18:
        if board[y - 1][x] == color : return 0
    # 가운데 6목체크
    else:
        if board[y + 5][x] == color or board[y - 1][x] == color : return 0

    return 1

def is_daegak_leftToright(y,x):
    # 현재 돌의 색상
    color = board[y][x]
    # 범위 넘을때
    if y + 4 >= 19 or x + 4 >= 19: return 0
    # 다른 값이 나올때
    for i in range(5):
        if board[y + i][x + i] != color : return 0
    # 6목일때
    # 제일 앞줄 6목 체크
    if y - 1 < 0 or x - 1 < 0:
        if board[y + 5][x + 5] == color: return 0
    # 제일 뒷줄 6목 체크
    elif y + 4 == 18 or x + 4 == 18:
        if board[y - 1][x - 1] == color : return 0
    # 가운데 6목체크
    else:
        if board[y + 5][x + 5] == color or board[y - 1][x - 1] == color : return 0

    return 1

def is_daegak_rightToleft(y,x):
    # 현재 돌의 색상
    color = board[y][x]
    # 범위 넘을때
    if y - 4 < 0 or x + 4 >= 19: return 0
    # 다른 값이 나올때
    for i in range(5):
        if board[y - i][x + i] != color : return 0
    # 6목일때
    # 제일 앞줄 6목 체크
    if y + 1 >= 19 or x - 1 < 0:
        if board[y - 5][x + 5] == color: return 0
    # 제일 뒷줄 6목 체크
    elif y - 4 == 0 or x + 4 == 18:
        if board[y + 1][x - 1] == color : return 0
    # 가운데 6목체크
    else:
        if board[y - 5][x + 5] == color or board[y + 1][x - 1] == color : return 0

    return 1




board = [list(map(int, input().split())) for _ in range(19)]
ret = 0
for y in range(19):
    for x in range(19):
        # 0이면 건너뛰자
        if board[y][x] != 0:
            if is_garo(y,x) or is_sero(y,x) or is_daegak_leftToright(y,x) or is_daegak_rightToleft(y,x):
                ret = board[y][x]
                ans = [y + 1, x + 1]
        if ret:
            break
    if ret:
        break
if ret:
    print(ret)
    s = ' '.join(map(str, ans))
    print(s)
else:
    print(0)

