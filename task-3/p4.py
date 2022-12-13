t = int(input())
for x in range(t):
    n=int(input())
    ai = list(map(int,input().split()))
    ai.pop()
    if ai.count(0)==len(ai):
        print(sum(ai))
    else:
        for i in ai:
           if i !=0:
               ai = ai[ai.index(i):]
               break

        print(ai.count(0) + sum(ai))
