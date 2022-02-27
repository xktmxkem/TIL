test_case = int(input(""))
for i in range(1,test_case + 1):
    p, q, r, s, w = map(int, input().split())
    a_cost = w*p
    if w > r :
        b_cost = q + ((w-r) * s)
    else:
        b_cost = q
    if a_cost > b_cost:
        print(f"#{i} {b_cost}")
    else:
        print(f"#{i} {a_cost}")
