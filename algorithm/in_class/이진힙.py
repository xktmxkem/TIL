
import heapq
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    heapq.heapify(lst)
    lst.insert(0,0)

    idx = len(lst)
    cnt = 0
    while(1):
        idx = idx // 2
        cnt += lst[idx]
        if idx < 1:
            break
    print(f'#{tc} {cnt}')