t = int(input(""))
ai = []
for x in range(t):
    n = int(input(""))
    ai = list(map(int,input("").split()))
    ai1 = ai[0]
    ai2 = ai[1]
    flag=0
    flag1=0
    for x in ai:
        if x % ai1 != 0:
            flag+=1
    for x in range(1,n):
        if ai[x] % ai2 != 0:
            flag1 += 1
    if flag ==0:
        print("YES")
    else:
        print("NO")
