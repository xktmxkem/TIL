test = int(input())
for test in range(1, test + 1):
    N = int(input())
    gravity = list(map(int, input().split()))
    max_ls = []
    for i in range(len(gravity) - 1):
        max_n = 0
        for j in range(i + 1, len(gravity) -1 ):
            if gravity[i] > gravity[j]:
                max_n += 1
 
        max_ls.append(max_n)
 
    print(f'#{test} {max(max_ls) + 1}')