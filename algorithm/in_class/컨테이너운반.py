t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)

    weight = 0
    c_idx = 0
    t_idx = 0
    while(c_idx != len(container)):
        if t_idx >= len(truck):
            break
        if truck[t_idx] >= container[c_idx]:
            weight += container[c_idx]
            t_idx += 1
            c_idx += 1
        else:
            c_idx +=1

    print(f'#{tc} {weight}')