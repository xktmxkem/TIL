

t = int(input())
for tc in range(1, t + 1):
    # 신청서
    N = int(input())
    # 스케줄
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))
    sort_work = sorted(work, key= lambda x:(x[1], x[0]))
    cnt = 0
    stack = []
    for i in range(len(sort_work)):
        if not stack:
            stack.append(sort_work[i][1])
            cnt += 1
        else:
            if stack[0] <= sort_work[i][0]:
                stack.pop()
                stack.append(sort_work[i][1])
                cnt += 1
    print(f'#{tc} {cnt}')