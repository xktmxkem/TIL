# 중복 눈금 인정
def dice(s, level,number = 1):
    global n
    if level == n:
        print(s)
        return
    for i in range(1, 7):
        dice(s + str(i), level + 1 , i)

# 중복 눈금 없음
def func(level) :
    if level == N :  # 0 1 2 3 ... N -1 / (총 N개 선택 ) N
        # 하나의 경우의 수가 만들어짐
        for i in range(N) :
            print(path[i],end = '' )
        print()
        return

    for i in range(1, 6 + 1):
        path[level] = i # 현재 level 에서 i 눈금 선택 후 ,
        func(level + 1)
        path[level] = 0 # 원상복구


N = int(input())
path = [0,0,0,0,0,0,0,0,0,0,]
func(0)


n = int(input())
visited = [0] * 7

dice2(s = '', level = 0)
