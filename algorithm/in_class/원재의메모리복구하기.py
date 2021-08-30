T = int(input())
for testcase in range(1, T + 1):
    before = input()
    cnt = 0
    compare = '0' 
    for i in before:
        if i == compare:
            continue
        else:
            cnt += 1
            compare = i
    print('#{} {}'.format(testcase, cnt))
