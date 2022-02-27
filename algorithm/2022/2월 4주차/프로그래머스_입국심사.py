def solution(n, times):
    times.sort()
    left = 1
    answer = times[-1] * n
    right = answer

    while left <= right:
        mid = (left + right) // 2
        temp = 0
        # 거스름돈 빼듯이 가장 작은거 부터 날린다
        for time in times:
            temp += mid // time
        if temp >= n:
            right = mid - 1
        else:
            left = mid + 1
    return left


n = 6
times = [7, 10]
solution(n, times)