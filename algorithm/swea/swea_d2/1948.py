test = int(input())
for test in range(test):
    month_1, day_1, month_2, day_2 = map(int, input().split())

    calender = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30 , 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    if month_1 == month_2:
        day = day_2 - day_1 + 1
    
    else:
        day = (calender[month_1] - day_1) + day_2 + 1

        for between in range(month_1 + 1, month_2 ):
            day += calender[between]
    
    print(f'#{test + 1} {day}')