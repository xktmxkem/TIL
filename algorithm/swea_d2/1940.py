test = int(input())
for test in range(1, test + 1):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(tc)]
    distance = 0
    speed = 0

    #전체 리스트 돌기
    for i in lst:
        # 입력이 하나일때 0 일때
        if len(i) == 1:
            distance += speed
        #두개일때 속도와 변속이  들어올때
        else:
            if i[0] ==1:
                speed += i[1]
                distance += speed
            elif i[0] ==2:
                speed -= i[1]
                #만약에 스피드가 더 떨어지면 0으로고정
                if speed < 0:
                    speed = 0
                distance += speed

    print(f'#{test} {distance}')