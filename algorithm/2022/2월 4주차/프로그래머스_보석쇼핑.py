#진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

# gems 배열의 크기는 1 이상 100,000 이하입니다.
# gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
# gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
# gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.

import heapq

def solution(gems):
    answer = []
    check = {}
    min_gems = len(set(gems))
    max_length = int(100001)

    len_gems = len(gems)
    len_check = 0
    temp = -int(21e8)
    for start_idx in range(len_gems + 1):
        if len(check) < min_gems:
            if start_idx < len_gems:
                try:
                    heapq.heappush(check[gems[start_idx]], -start_idx)
                except:
                    check[gems[start_idx]] = [-start_idx]
                    len_check += 1
        else:
            name = ''
            for keys in check.keys():
                if temp < check[keys][0]:
                    temp = check[keys][0]
                    name = keys
            if start_idx < len_gems:
                try: heapq.heappush(check[gems[start_idx]], -start_idx)
                except: check[gems[start_idx]] = [-start_idx]
            answer.append([start_idx - (-temp + 1), -temp + 1, start_idx])

    answer.sort()
    print([answer[0][1], answer[0][2]])
    return [answer[0][1], answer[0][2]]


gems = ['a', 'b', 'c', 'a', 'd', 'b', 'f']

solution(gems)

