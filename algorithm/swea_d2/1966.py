
# 테스트 케이스 수 입력
test_case = int(input())

# 입력한 테스트 케이스 만큼
for test in range(1, test_case + 1):

    # 리스트 길이 초기화
    # 만약 숫자 갯수가 틀리면 에러발생 위해서 
    length = int(input())  
    result_ls = [0] * length

    # 들어온 숫자를 리스트형으로 저장
    sort_ls = list(map(int, input().split()))
    # 저장한 리스트를 정렬 sorted는 반환값이 있다 
    # 속도는 sort가 훨씬 빠르긴함 
    sort_ls = sorted(sort_ls)

    # 들어온 리스트를 순서대로 초기화한 리스트에 할당
    # 여기서 인데스가 안맞으면 에러가남 
    # 정렬된 채로 할당된 result_ls를 문자열로 반환
    for i in range(len(result_ls)):
        result_ls[i] = str(sort_ls[i])
    result_str = ' '.join(result_ls)

    # 출력 
    print(f'#{test} {result_str}')
