import sys

# 표준 입력을 파일로 설정하기 -> input.txt를 읽어들여옴
sys.stdin = open("input.txt", "r")

def find(N, M, TREES):
    TREES.sort()
    left = 0
    right = TREES[-1]
    while left <= right:
        mid = (left + right) // 2
        meter = 0
        for tree in TREES:
            if tree > mid:
                meter += (tree - mid)

        # 예상보다 너무 많이 meter를 가져갈 경우 더 높은 위치에서 잘라야함
        if meter < M:
            right = mid - 1
        # 반대의 경우 더 작은곳에서 잘라야함
        else:
            left = mid + 1

    return right


# N : 나무의 수, M : 필요한 나무 길이
N, M = map(int, input().split())
TREES = list(map(int, input().split()))
answer = find(N, M, TREES)
print(answer)