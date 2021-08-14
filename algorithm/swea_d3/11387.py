test = int(input())
for test in range(1, test + 1):
    d, l, n = map(int, input().split())
    dmg = 0
    ## 첫빵은 데미지 0이 핵심 
    for i in range(n):
       dmg += d + d *i * (l / 100)
    print(f'#{test} {dmg}')
