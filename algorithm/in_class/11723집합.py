import sys

sys.stdin = open("text.txt","r")


T = int(sys.stdin.readline())

S = 1 << 21
de = -1
for _ in range(T):
    temp = sys.stdin.readline().split() # list
    if len(temp) == 2:
        cmd = temp[0]
        x = int(temp[1])
    else :
        cmd = temp[0]

    if cmd == "add":
        S |= (1<<x)
    elif cmd == "remove":
        S &= ~(1 << x)
    elif cmd == "check": # x 번째 원소가 있는지 체크
        print((S & (1 << x)) >> x )
    elif cmd == "toggle":
        S ^= (1 << x)
    elif cmd == "all":
        S = (1 << 21) - 1
    elif cmd == "empty":
        S = 1 << 21