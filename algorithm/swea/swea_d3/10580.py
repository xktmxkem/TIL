test = int(input())
for test in range(1, test + 1):
    # 전선 수 
    line = int(input())
    # 전선 딕셔너리 임시 선언
    dict_pole = {}

    # key, value 형태로 넣음
    for i in range(line):
        a, b =  map(int, input().split())
        dict_pole[a] = b
    
    # 전체수 세기 위한 코드
    count = 0

    # 첫번째 전선과 나머지 비교, 단 이때 중복되어 수는 2배가 됨
    for a, b in dict_pole.items():
        for x, y in dict_pole.items():
            # 비교 대상이 둘다 크거나 혹은 둘다 작거나 일때는 카운트 되지 않음
            # 그 이외에 일때만 카운트
            # 같은 수는 안들어오나 혹시 몰라 = 으로 선언
            if a > x and b > y:
                continue
            elif a <= x and b <= y:
                continue
            else:
                count += 1

    print(f'#{test} {int(count/2)}')