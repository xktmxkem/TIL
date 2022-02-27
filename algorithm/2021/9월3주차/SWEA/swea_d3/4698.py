test = int(input())
for i in range(1,test+1):
    D, A, B = map(int, input().split())
    temp_ls = []
    temp_mls = []
    for num in range(A, B + 1):
        if str(D) in str(num):
            temp_ls.append(num)
    
    for num in temp_ls:
        for check in range(2, num):
            if num % check == 0:
                temp_mls.append(num)
    
    temp_mls = list(set(temp_mls))

    result_num = len(temp_ls) - len(temp_mls)

    print(f'#{i} {result_num}')