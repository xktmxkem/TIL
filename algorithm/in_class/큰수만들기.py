



def solution(number, k):
    answer = ''
    pick = len(number) - k

    now_idx = 0
    for i in range(pick, 0, -1):
        if i != 1:
            temp = max(number[now_idx: -i + 1])
            answer += temp
            number = number[number.index(temp) + 1:]
        else:
            answer += max(number[now_idx:])
    return answer

number = '1231234'
k = 3
solution(number,k)

