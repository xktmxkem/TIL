test = int(input())
for testcase in range(1, test + 1):
    p = input().rstrip()
    q = input().rstrip()


    result = 'Y'

    if  p + 'a' == q:
        result = 'N'

    print('#{} {}'.format(testcase, result))
