T = int(input())
for testcase in range(1 , T + 1):
    s = input()

    for i in range(1,11):
        start = 0
        end = 0
        cnt = 1
        ret = 0
        start = i * cnt
        end = i * (cnt + 1)
        cnt += 1
        for j in range(30//i):
            if s[:i] != s[start:end]:
                break
        else:
            ret = 1

        if ret:
            print('#{} {}'.format(testcase, i))
            break
