# 인수분해 하는식으로 제곱수인지 아닌지 판별해보자
# 소수의 리스트를 반환
def prime(number):
    # 에라토스 테네스의 체 초기화 : num의 갯수만큼 true리스트를 만든다
    lst = [True] * number
    # 이부분은 물어보기... 왜 루트만봐도 되는지 이해가안됨 아직
    length = int(number ** 0.5)
    for i in range(2 , length + 1):
        # 배수해서 false하면 자동적으로 넘김
        if lst[i] == True:
            #i배수부분을 다 없앰
            for j in range(i + i, number, i):
                lst[j] = False
    # false인 부분만 숫자로 만들어서 출력
    return_lst = []
    for i in range(2, number):
        if lst[i] == True:
            return_lst.append(i)
    return  return_lst



test = int(input())
for test in range(1, test + 1):
    num = int(input())
    prime_num = prime(num)
    prime_dict = {}
    for i in prime_num:
        prime_dict[i] = 0



    prime_index = 0
    while(prime_index < len(prime_num) - 1):
        if num % prime_num[prime_index] == 0:
            # 나눈 몫을 남긴다
            num = num // prime_num[prime_index]
            # 딕셔너리에 해당 소수를 숫자를 추가한다.
            prime_dict[prime_num[prime_index]] += 1
        # 나눈 나머지가 존재할시 == 나눠지지 않을시
        else:
            #반복수를 줄임
            if num == 1:
                break
            prime_index += 1
    #최종 제출용 변수
    #만약 소인수 분해가 되지않는 소수라면 자기자신을 출력 아니라면 소인수분해 값을 출력
    min_num = 1
    check_value = 0


    for key, value in prime_dict.items():
        # 소인수 분해의 결과값이 홀수라면
        if value % 2 != 0:
            check_value += 1
            min_num *= key

    # check_value가 0이 아니라면, 즉 소인수 분해가 하나라도 되었다면
    if check_value:
        print(f'#{test} {min_num}')
    else:
        print(f'#{test} {min_num * num}')

