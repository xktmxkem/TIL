
test_case = int(input())
for test_case in range(1, test_case + 1):

    a = int(input())
    
    temp_ls = []
    for x in range(a):
        #2차원 리스트 첫줄 둘째줄 미리 넣어둠
        if x == 0:
            temp_ls.append([1])
        if x == 1:
            temp_ls.append([1,1])
        # 이후부터 숫자 넣기 시작
        if x > 1:
            # 더한 리스트 만들기 위한 임시 리스트 선언
            add_list = []
            
            for y in range(x + 1): 
                # 만약 첫번째 인덱스라면 1 추가
                if y == 0:
                    add_list.append(1)
                # 끝 인덱스라면 1을 추가한 후 전체 리스트를 temp_ls에 추가
                elif y == x:
                    add_list.append(1)
                    temp_ls.append(add_list)
                #아니라면 temp_ls에 담긴 제일 리스트의 인덱스와 전인덱스 합친값을 추가
                else:
                    add_list.append(temp_ls[-1][y] + temp_ls[-1][y-1])
    
    print(f'#{test_case}')
    #마지막으로 temp_ls를 출력
    #요소의 끝이라면 다음줄로 개행
    #아니라면 공백 붙여서 출력
    for first in temp_ls:
        for second in range(len(first)):
            if second == len(first) - 1:
                print(first[second])
            else:
               print(first[second], end = ' ')
        

