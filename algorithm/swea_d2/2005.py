
test_case = int(input())
for test_case in range(1, test_case + 1):

    a = int(input())
    
    temp_ls = []
    for x in range(a):
        if x == 0:
            temp_ls.append([1])
        if x == 1:
            temp_ls.append([1,1])
        if x > 1:
            add_list = []
            for y in range(x + 1): #3
                if y == 0:
                    add_list.append(1)
                elif y == x:
                    add_list.append(1)
                    temp_ls.append(add_list)
                else:
                    add_list.append(temp_ls[-1][y] + temp_ls[-1][y-1])
    
    print(f'#{test_case}')
    for first in temp_ls:
        for second in range(len(first)):
            if second == len(first) - 1:
                print(first[second])
            else:
               print(first[second], end = ' ')
        

