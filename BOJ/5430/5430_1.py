'''
 메모리: 38836 KB, 시간: 340 ms
 2022.04.27
 by Alub
'''
tc = int(input())
for i in range(tc):
    orders = input()
    n = int(input())
    try:
        lst = list(map(int, input()[1:-1].split(',')))
    except:
        lst = []
    #거꾸로인지 아닌지
    flag = True
    # 앞에서 삭제한 양
    left = 0
    # 뒤에서 삭제한 양
    right = len(lst) - 1
    # 답
    answer = 0
    for order in orders:
        if order == "R":
            if flag:
                flag = False
            else:
                flag = True
        else:
            if 0 <= left < len(lst) and 0 <= right < len(lst):
                if flag:
                    lst[left] = 0
                    left += 1
                else:
                    lst[right] = 0
                    right -= 1
            else:
                answer = 1
                break
    if answer:
        print("error")
    else:
        if flag:
            print(str(lst[left:right+1]).replace(" ",""))
        else:
            print(str(lst[left:right+1][::-1]).replace(" ",""))
