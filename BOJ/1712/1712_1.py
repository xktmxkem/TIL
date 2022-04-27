'''
 메모리: 30840 KB, 시간: 72 ms
 2022.04.28
 by Alub
'''
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(A//(C - B) + 1)