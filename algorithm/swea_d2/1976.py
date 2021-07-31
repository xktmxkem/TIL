test = int(input())
for test in range(1, test + 1):
    hour_1, min_1, hour_2, min_2 = map(int, input().split())
    result_ls = []
    hour = hour_1 + hour_2
    min = min_1 + min_2



    # &과 and 차이 질문 

    if hour <= 12 and min < 60:
        result_ls.append([hour,  min])

    elif hour > 12 and min < 60:
        result_ls.append([hour - 12, min])

    elif hour > 12  and min >= 60:

        result_ls.append([hour-11, min-60])

    elif  hour <= 12 and min >= 60:
        if hour == 12:
            result_ls.append([1, min - 60])
        else:
            result_ls.append([hour + 1, min - 60])

    result_ls =list(map(str ,sum(result_ls, [])))
    result = ' '.join(result_ls)
    print(f'#{test} {result}')


