n = int(input())
for i in range(1, n+1):
    temp = input()
    cnt= 0
    for j in range(2,31):
        if len(set(temp)) == 1:
            cnt = 1
            break
        elif temp[:j] == temp[j:2*j] :
            cnt = j
            break
    print(f'#{i} {cnt}')