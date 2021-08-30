from collections import deque

def cheeze(n, m):
    # 처음에 화덕의 개수만큼 들어가야됨 피자가
    for i in range(n):
        queue.append(pizza[i])

    # 초기 화덕 채우고 남은 피자 중 가장 먼저 들어와야할 피자
    # 인덱스상 n번의 피자가 들어가야한다, n-1번까지 들어감
    start_idx = n

    # 화덕에 피자가 하나 남을 때까지
    while(len(queue) > 1):
        ret = queue.popleft()
        # 남은 피자는 화덕에서 하나씩 빠질때 추가되어야 한다, 만약 더이상 추가할 피자가 없으면 화덕에 자리가 하나씩 남게된다
        if ret[1] == 1 and start_idx < m:
            queue.append(pizza[start_idx])
            start_idx += 1

        # 만약 치즈가 덜녹았다면 반 나눠서 끝에 추가해준다
        if ret[1] > 1:
            ret[1] = ret[1] // 2
            queue.append(ret)

    return 0






test = int(input())
for testcase in range(1, test + 1):
    # n 화덕의 크기
    # m 피자 개수
    queue = deque()
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    pizza = []
    for idx, value in enumerate(lst):
        pizza.append([idx + 1, value])

    cheeze(n, m)

    result = queue.popleft()
    print('#{} {}'.format(testcase, result[0]))
