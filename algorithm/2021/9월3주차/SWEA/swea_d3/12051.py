test = int(input())
for test in range(1, test + 1):
    # 반올림x
    # n : 오늘한 게임의 최대 수 (정확히 모름)
    # pd : 오늘 한 게임중 이긴 승률
    # pg : 예전에 한 게임중 이긴 승률
    # possible_n : 가능한 오늘한 판수 및 승수
    n, pd, pg = map(int, input().split())

    # 1 : possible, 2 : broken
    possible_pg = 1

    possible_pd = 0

    # n이 100 이상이면 100일 경우에 어떻게든 하나를 만들수 있음
    if n < 100:
        for i in range(1, n + 1):
            if (pd * i) % 100 == 0:
                possible_pd = 1
    else:
        possible_pd = 1

    # 만약 승률이 100퍼라면
    if pg ==100:
        # 오늘한 게임의 승률이 100퍼가 아니면 고장
        if pd != 100 :
            possible_pg = 0
    # 만약 승률이 0퍼라면
    elif pg == 0:
        #오늘 단 한판이라도 이기면 고장
        if pd != 0:
            possible_pg = 0
    else:
        if possible_pd == 0 :
            possible_pg = 0


    if possible_pg:
        print('#{} Possible'.format(test))
    else:
        print('#{} Broken'.format(test))


