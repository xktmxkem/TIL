test = int(input())
for test in range(1, test + 1):
    money = int(input())

    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    
    # 위의 돈이 들어가며 몪을 리스트에 추가함 
    for change in change:
        
        result.append((money//change)) 
        # 만약 돈이 나눠줄 돈보다 크다면 빼준 만큼을 money에 저장함
        if money >= change:
            money -= (change * (money//change))

    # 몫이 저장된 리스트 result를 join을 통해 원하는 문자열로 만들어줌
    result_1 = " ".join(list(map(str, result)))
    print(f'#{test}\n{result_1}')

