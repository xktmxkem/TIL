
def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0
    boat = 0
    while people:
        now = people.pop(0)
        boat += now
        for i in range(len(people)):
            if boat + people[i] <= limit:
                del people[i]
                break
        cnt += 1
        boat = 0

    answer = cnt
    return answer


people = [100, 500, 500, 900, 950]
limit = 1000
solution(people, limit)

