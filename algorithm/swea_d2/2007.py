n = int(input())
for i in range(1, n+1):
    temp = input()
    cnt= 0
    for j in range(2,31):
        # 하나의 문자만 들어있을경우 전체 수는 1
        if len(set(temp)) == 1:
            cnt = 1
            break
        # 문자열 슬라이스로 2배씩 찾아가며 비교 
        elif temp[:j] == temp[j:2*j] :
            cnt = j
            break
    print(f'#{i} {cnt}')