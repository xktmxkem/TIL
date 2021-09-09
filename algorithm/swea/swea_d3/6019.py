import math

test = int(input())
for test in range(1, test + 1):
    D, A, B, F = map(int, input().split())
    time = (D / (A + B))

    F_distance = time * F



    print(f'#{test} {F_distance:.6f}')

     