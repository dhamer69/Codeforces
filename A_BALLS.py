t=int(input())
while(t>0):
    n=int(input())
    s=input()
    
    ctr=0
    ctb=0
    ctg=0
    for i in s:
        if i=="R":
            ctr+=1
        elif i=="G":
            ctg+=1
        else:
            ctb+=1
    if ctg==n or ctr==n or ctb==n:
        print(n)
    else:
        print(max(ctr,ctb,ctg)+1)
    t-=1