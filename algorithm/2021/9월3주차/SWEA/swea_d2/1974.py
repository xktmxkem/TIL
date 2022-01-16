#테스트케이스
def sudoqu_check(sudoqu):
    compare_list = [i for i in range(1,10)]

#############가로#########  
    for hori in sudoqu:

        sort_hori = sorted(hori)
        if sort_hori != compare_list:
            return 0
##############세로#######
    for idx in range(9):
        vert_ls = []
       
        for verti in sudoqu:
            vert_ls.append(verti[idx])
      
        vert_ls = sorted(vert_ls)
        if vert_ls != compare_list:
            return 0


############큐브###########
    temp_ls = []
    for i in sudoqu:
        temp_ls.append([i[0:3],i[3:6],i[6:9]])

    a = []
    b = []
    c = []
    for i in temp_ls:
        ### for문 가독성 ###
        a.append(i[0])
        b.append(i[1])
        c.append(i[2])
        if len(a) == 3:
            a = sorted(sum(a, []))
            b = sorted(sum(b, []))
            c = sorted(sum(c, []))
            if a != compare_list or b!= compare_list or c != compare_list:
                return 0
            else:
                a = []
                b = []
                c = []
    return 1




        

            


test_case = int(input())
for test in range(1, test_case + 1):
    sudoqu = []
    for i in range(9):
        sudoqu.append(list(map(int, input().split())))

    print(f'#{test} {sudoqu_check(sudoqu)}')

            

