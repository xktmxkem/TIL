test = int(input())
for test in range(1, test + 1):
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print('#{} -1'.format(test))
    else:
        print('#{} {}'.format(test, (a * b)))