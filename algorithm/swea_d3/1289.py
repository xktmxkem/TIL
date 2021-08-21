test = int(input())
for test in range(1, test + 1):
    bit = input()
    final_bit = []
    # 2중for문을 사용하지 않기 위해 단일 for문으로 구성
    #str형 리스트로 만들어 순차적으로 비교
    for bit in bit:
        final_bit.append(bit)


    before_bit = ['0'] * len(final_bit)


    cnt = 0

    for i in range(len(final_bit)):
        # 최종 비트와 변경한 비트가 같다면 break
        if final_bit == before_bit:
            break
        else:
            #만약 해당 위치의 비트가 최종비트의 값과 다르다면 그 이후의 값까지
            #index slicing을 통해 해당 위치 비트의 값으로 이루어진 list를 넣어줌
            # 이후 cnt를 추가함
            if before_bit[i] != final_bit[i]:
                before_bit[i:] = [final_bit[i]] * (len(before_bit) - i)
                cnt += 1

    ## 실행시간을 더 줄일수 잇는지 조사 
    print('#{} {}'.format(test, cnt))