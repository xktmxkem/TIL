
def solution(name):
    answer = 0
    ans_lst = []

    min_change = []
    for i in name:
        min_change.append(min(ord(i) - ord('A'), 26 - (ord(i) - ord('A'))))
    print(min_change)

    sum_min = sum(min_change)
    sum_right = 0
    sum_left = 0



    cnt = 0

    for i in range(len(min_change)):
        if min_change[i] != 0:
            sum_right += min_change[i]

        if min_change[-i] != 0:
            sum_left += min_change[-i]
        if sum_right == sum_min or sum_left == sum_min:
            break
        cnt += 1

    return answer

name = "ZZAAAZZ"
solution(name)
