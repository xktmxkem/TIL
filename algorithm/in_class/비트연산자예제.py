import sys
sys.stdin = open("text.txt","r")


str_bin = input()

a = 0
while a < len(str_bin):
    temp = str_bin[a+0: a+7]
    print(int(temp, 2),end = ',')
    a += 7