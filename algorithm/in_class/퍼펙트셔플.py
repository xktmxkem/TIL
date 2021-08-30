test = int(input())
for testcase in range(1 , test + 1):
    n = int(input())
    lst = list(input().split())
    odd = 0
    if len(lst) % 2:
        odd = 1
        lst_a = lst[:(len(lst) // 2) + 1]
        lst_b = lst[(len(lst) // 2) + 1:]
    else:
        lst_a = lst[:(len(lst) // 2)]
        lst_b = lst[(len(lst) // 2) :]

    s= ''
    for i in range(len(lst_b)):
        s += ' ' + lst_a[i] + ' ' + lst_b[i]

    if odd:
        s +=' ' + lst_a[-1]
        print('#{}{}'.format(testcase, s))
    else:
        print('#{}{}'.format(testcase, s))