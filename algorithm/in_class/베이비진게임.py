def check(player, card):
    if player[card] == 3:
        return True

    for i in range(8):
        if player[i] and player[i+1] and player[i+2]:
            return True

    return False




t = int(input())
for tc in range(1, t + 1):
    lst = list(map(int, input().split()))
    p1 = [0 for _ in range(10)]
    p2 = [0 for _ in range(10)]

    ans = 0
    for i in range(6):
        p1_card = lst[2*i]
        p2_card = lst[2*i + 1]

        p1[p1_card] += 1
        p2[p2_card] += 1

        if i >= 2:
            if check(p1, p1_card):
                ans = 1
                break

            elif check(p2, p2_card):
                ans = 2
                break

    print(f'#{tc} {ans}')







