t = int(input())
for tc in range(1, t+1):
    number = float(input())
    cnt = 0
    now = 1
    total = 0
    ans = ''
    while(1):
        cnt += 1
        now /= 2
        if number == 0:
            break
        if cnt > 13:
            ans = 'overflow'
            break
        if now <= number:
            number -= now
            ans += '1'
        else:
            ans += '0'

    print(f'#{tc} {ans}')

# dfs사용 시간복잡도 고민
import sys
sys.stdin = open("text.txt","r")


def func(level, sum , bits) : #sum(float로 계산) , bits는 1또는 0을 붙여나간다
    if level == 13 :
        #print(sum, ":" , bits)
        MAP[str(sum)] = bits
        return

    func(level + 1, sum + (0.5) ** level, bits + '1'  ) # 현재 level bit를 선택 o
    func(level + 1, sum , bits + '0') # 현재 level bit를 선택 x


def erase_zero(s):
    lst = []
    check = 0
    for i in range(len(s) -1, -1 , -1 ) :
        if s[i] == '1':
            check = 1
        if check == 1:
            lst.append(s[i])

    ret = ""
    while lst :
        ret += lst.pop()

    return ret

MAP = dict()
func(1, 0, '')
de = - 1

T = int (input())
for tc in range(1, T+ 1):
    key = input()
    if key in MAP:
        val = MAP[key]
        val = erase_zero(val)
        print("#{} {}".format(tc, val))
    else :
        print("#{} overflow".format(tc))