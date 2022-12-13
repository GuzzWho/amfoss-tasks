t = int(input(""))
ai = []
for x in range(t):
    n = int(input(""))
    ai = list(map(int, input("").split()))
    flag = len(set(ai)) == len(ai)
    flag0 = ai.count(0)
    if (flag) and flag0 == 0:
        mana = n + 1
    elif flag0 != 0:
        mana = n - flag0
    else:
        mana = n
    print(mana)
