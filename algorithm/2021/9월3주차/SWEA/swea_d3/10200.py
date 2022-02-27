test = int(input())
for test in range(test):
    n, a, b = map(int, input().split())
    if n > (a+b):
        print(f'#{test + 1} {min(a, b)} 0')
    else:
        print(f'#{test + 1} {min(a, b)} {(a + b - n)}')