test = int(input())
for test in range(1, test + 1):
    lst = list(map(int, input().strip()))

    num = [0] * 10
    for var in range(len(lst)):
        num[lst[var]] += 1

    cnt = 0
    i = 0
    while (i < 10):
        if num[i] >= 3:
            cnt += 1
            num[i] -= 3
            continue
        if i < 8:
            if num[i] >= 1 and num[i + 1] >= 1 and num[i + 2] >= 1:
                cnt += 1
                num[i] -= 1
                num[i + 1] -= 1
                num[i + 2] -= 1
                continue
        if cnt == 2:
            break
        i += 1

    if cnt == 2:
        print(f'#{test} Baby Gin')

    else:
        print(f'#{test} Lose')