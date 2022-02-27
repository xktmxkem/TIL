def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance

    answer = 0
    while left <= right:
        prev = 0
        # 최종 제출 거리
        mins = int(21e8)
        remove = 0

        # 기준이 되는 최소 거리
        mid = (left + right) // 2
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                remove += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]

        # 삭제가 더 많이 되었다
        # 즉, 최소 거리가 예상보다 더 크게 되었다.
        # 따라서 right를 mid 왼쪽으로 옮겨 기준 최소 거리를 짧게 만든다
        if remove > n:
            right = mid - 1
        # 반대의 경우 삭제가 덜 되었다,
        # 따라서 기준 최소 거리를 좀더 크게 잡기 위해 옮겨준다
        else:
            answer = mins
            left = mid + 1
    print(float("inf"))
    return answer



distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
solution(distance, rocks, n)