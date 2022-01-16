test = int(input())
for test in range(1, test +1):
    num = int(input())
    result = 0
    #짝수면 - 홀수면 +
    for j in range(1, num+1):
        if j % 2:
            result += j
        else:
            result -= j
    print(f'#{test} {result}')
