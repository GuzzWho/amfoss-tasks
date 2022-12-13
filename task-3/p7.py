n=input("")
count =0
while int(int(n)/10) != 0:
    s = 0
    for x in n:
        s += int(x)
    count += 1
    n = str(s)
print(count)
