test = int(input())
for test in range(1, test + 1):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(tc)]
    distance = 0
    speed = 0
    for i in lst:
        if len(i) == 1:
            distance += speed
        else:
            if i[0] ==1:
                speed += i[1]
                distance += speed
            elif i[0] ==2:
                speed -= i[1]
                if speed < 0:
                    speed = 0
                distance += speed

    print(f'#{test} {distance}')