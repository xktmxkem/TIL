test = int(input())
for test in range(test):

    # 받아올 알파벳 수
    n = int(input())

    alpha_dict = {}
    
    # 딕셔너리에 넣어옴
    for alpha in range(n):
        key, value = input().split()
        alpha_dict[key] = int(value)

    
    # 10개가 되면 다음줄로 다끝나면 다음줄로 개행
    print(f'#{test + 1}')
    length = 0
    for alpha in alpha_dict.keys():
        for number in range(alpha_dict[alpha]):
            print(alpha , end = '')
            length += 1
            if length == 10:
                length = 0
                print()
    print()

