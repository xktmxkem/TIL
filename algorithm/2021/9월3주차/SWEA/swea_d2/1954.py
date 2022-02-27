
def snail(num):


    #### 중요포인트 swallow 복사 ## 시간많이버림
    #result_ls = [[0] * snail] * snail


    ##초기화
    result_ls = []
    for i in range(num):
        result_ls.append([0]*  num)
    hori_point = 0  # x 좌표
    verti_point = 0 # y 좌표
    flag = True # 순서용 깃발
    number = 1 # 자료에 넣기 위한 값 
    length = num # length 는 n -> n-1 n-1 > n-2 n-2 > 0순으로 줄어드는 가로 세로 길이를 지속적으로 가지기 위한 변수

    
    # 가로 세로 넣어야 될 값이 0이 되면종료
    while(length > 0):

    ## 첫줄 가로 유일하게 한번만들어가야되서 따로 분기
        if length == num:
            for first in range(length):
                result_ls[0][first] = number
                hori_point = first
                number += 1
                flag = False
            length -= 1

        ## 이후 함수 반복
        else:
            # falg False일때는 y축 감소(인덱스상 증가)
            if flag == False:
                for verti in range(length):
                    verti_point += 1
                    result_ls[verti_point][hori_point] = number
                    number += 1
  
 
            # x축 증가(인덱스상 감소)
                for hori in range(length, 0, -1):
                    hori_point -= 1
                    result_ls[verti_point][hori_point] = number
                    number += 1
  
                # 한번만 변경해야하기에 for문 밖에 넣는다
                flag = True
                length -= 1


            # flag True일때는 반대로 작동 
            else:
                for verti in range(length , 0, -1):
                    verti_point -= 1
                    result_ls[verti_point][hori_point] = number
                    number += 1

                for hori in range(length):
                    hori_point += 1
                    result_ls[verti_point][hori_point] = number
                    number += 1
                flag = False
                length -= 1


    return result_ls  

    ###출력###
test = int(input())
for test in range(test):
    num = int(input())
    result_ls = snail(num)
    print(f'#{test + 1}')
    for i in result_ls:
        print(*i)




