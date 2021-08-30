def check(y, x):
    global ret
    # x 체크
    x_len = 0
    y_len = 0
    max_sum = 0
    for i in range(w):
        if x + i >= w:
            break
        if ground[y][x + i] == 0:
            break
        x_len += 1

    for j in range(h):
        if y + j >= h:
            break
        if ground[y + j][x] == 0:
            break
        y_len += 1

    for i in range(y_len):
        for j in range(x_len):
            max_sum += ground[y +i ][x + j]

    if ret < max_sum:
        ret = max_sum

    return 0


T = int(input())
for testcase in range(1, T + 1):
    # h = y, w = x
    h, w = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(h)]
    ret = 0
    for y in range(h):
        for x in range(w):
            if ground[y][x] != 0:
                check(y,x)
    print('#{} {}'.format(testcase, ret))
