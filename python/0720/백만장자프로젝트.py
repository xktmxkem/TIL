test_case = int(input())
for i in range(test_case):

    day = int(input())
    day_list = [0] * day
    day_list = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for j in range(len(day_list)):
        for x in range(len(day_list)):
            if day_list[j] >= day_list[x]:
                continue
            else:
                
    print(day_list)