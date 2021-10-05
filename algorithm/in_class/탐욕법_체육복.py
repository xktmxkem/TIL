def solution(n, lost, reserve):
    answer = 0
    student = [1] * (n + 1)
    for i in lost:
        student[i] -= 1

    for i in reserve:
        student[i] += 1

    for i in range(len(student)):
        if student[i] == 0:
            if i < n:
                if student[i - 1] == 2:
                    student[i] = 1
                    student[i- 1] = 1

                elif student[i + 1] == 2:
                    student[i] = 1
                    student[i + 1] = 1
            else:
                if student[i - 1] == 2:
                    student[i] = 1
                    student[i- 1] = 1

    for i in range(1, len(student)):
        if student[i] != 0:
            answer += 1
    return answer

n = 5
lost = [1,3,4]
reserve = [1,3]
ans = solution(n, lost, reserve)
print(ans)