n = input()
si = list(map(int, input().split()))
c1 = si.count(1)
c2 = si.count(2)
c3 = si.count(3)
c4 = si.count(4)
if c3 == c1:
    if c2 % 2 == 0:
        print(int(c4 + c3 + (c2 / 2)))
    else:
        print(int(c4 + c3 + (c2 // 2) + 1))
elif c3 < c1:
    c4 = c4 + c3
    c1 = c1 - c3
    c3 = 0
    k2 = int(c1 / 2)
    c1 = int(c1 / 2) + (c1 % 2)
    c2 = c2 + k2
    c1 = c1 - k2
    k3 = int(c2 / 2)
    c2 = int(c2 / 2) + (c2 % 2)
    c4 = c4 + k3
    c2 = c2 - k3
    if c1==c2:
        c1=0
    k1 = int(c1 / 4)
    c1 = int(c1 / 4) + (c1 % 4)
    c4 = c4 + k1
    c1 = c1 - k1
    print(c1 + c2 + c3 + c4)
elif c3 > c1:
    if c2 % 2 == 0:
        print(int(c4 + c1 + (c2 / 2) + (c3 - c1)))
    else:
        print(int(c4 + c1 + (c2 // 2) + 1 + (c3 - c1)))