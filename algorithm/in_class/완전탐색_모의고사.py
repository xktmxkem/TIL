def solution(answers):
    # 가장 많은 문제를 맞힌 사람을 나타내는 리스트
    answer = []
    # 수포자 1
    supo_1 = [1, 2, 3, 4, 5]
    # 수포자 2
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 수포자 3
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자가 맞은 수를 기록하는 배열
    cnt = [0, 0, 0]

    # 입력받은 답안을 토대로 각 수포자가 얼마나 맞았는지 탐색
    for i in range(len(answers)):
        # 수포자 1은 5를 주기로 반복
        if answers[i] == supo_1[i % 5]:
            cnt[0] += 1
        # 수포자 2는 8을 주기로 반복
        if answers[i] == supo_2[i % 8]:
            cnt[1] += 1
        # 수포자 3은 10을 주기로 반복
        if answers[i] == supo_3[i % 10]:
            cnt[2] += 1

    # 가장 많이 맞춘 수
    max_cnt = max(cnt)

    # 가장 많이 맞춘 사람을 배열에 담기
    for i in range(3):
        # 가장 많이 맞춘 수와 같은 cnt 요소의 인덱스를 +1 하여 answer에 담기
        if max_cnt == cnt[i]:
            answer.append(i + 1)

    return answer


print(solution([1, 3, 2, 4, 2, 2, 3, 1, 4, 5, 2, 3, 4]))