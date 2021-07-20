from collections import Counter


testcase = int(input(''))
score = []

for i in range(1,testcase+1):
    count = int(input(''))
    score = list(map(int, input("").split()))
    cnt = Counter(score)
    cnt_most = cnt.most_common()
    cnt_most_doutble =[0] * 100
    for i in range(len(cnt_most)):
        if cnt_most[0][1] == cnt_most[i][1]:
            cnt_most_doutble[i] =cnt_most[i][0]
    print(f"#{count} {max(cnt_most_doutble)}")
