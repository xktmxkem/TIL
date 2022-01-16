def part_set_function(number):

    result_lst = []
    for i in range(1<<number):
        temp_lst = []
        for j in range(number):
            if i & (1 <<j):
                temp_lst.append(j)

        result_lst.append(temp_lst)
    print(result_lst)
    return result_lst



test = int(input())
for test_case in range(1, test + 1):

    # n은 입력 받을 수 , l은 제한 칼로리
    n, l = map(int, input().split())

    # 두 리스트 선언 인덱스 접근 위해, 딕셔너리로 했다가 runtime 에러
    like_lst = []
    cal_lst = []
    # 칼로리 제한 내의 부분집합을 담을 리스트
    part_set = []
    # 최고 선호도 변수
    best_like = 0


    for i in range(n):
        like, cal = map(int, input().split())
        like_lst.append(like)
        cal_lst.append(cal)

    # 부분집합
    part_set = part_set_function(10)


    for part in part_set:
        sum_like = 0
        check_cal = 0
        for num in part:
            check_cal +=  cal_lst[num]
            if check_cal > l:
                sum_like = 0
                break
            sum_like += like_lst[num]

        if best_like < sum_like:
            best_like = sum_like


    print('#{} {}'.format(test_case, best_like))


