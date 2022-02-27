for test in range(1, 10 + 1):
    num = int(input())
    #index out of 방지 위해 복사를 해둔다, 단순 입력을 이용하기 위함

    build_ls = [0] * num
    build_input = list(map(int, input().split()))
    house = 0
    for i in range(num):
        build_ls[i] = build_input[i]

    for i in range(2, len(build_ls) - 2):
        if build_ls[i] > build_ls[i-1] and build_ls[i] > build_ls[i-2] and build_ls[i] > build_ls[i+1] and build_ls[i] > build_ls[i+2]:
            house += (build_ls[i] - max(build_ls[i-1], build_ls[i-2], build_ls[i+1], build_ls[i+2]))

    print(f'#{test} {house}')