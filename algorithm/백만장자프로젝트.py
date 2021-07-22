def recur(temp_list):
    if len(temp_list) < 2:
        print('끝')
        return 0
    else:
        max_index = temp_list.index(max(temp_list))
        finish_list = temp_list[:+1]
        recur(temp_list[max_index:])
        print(finish_list)
        


recur([10, 7, 6])

# test_case = int(input())
# for i in range(test_case):

#     day = int(input())
#     day_list = [0] * day
#     day_list = list(map(int, input().split()))
#     sum = 0
#     cnt = 0

                
#     print(day_list)