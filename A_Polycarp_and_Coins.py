t=int(input())
while(t>0):
    n=int(input())
    c1=0
    c2=0
    # let diff is 0
    if n%3==0:
        c1=int(n/3)
        c2=int(n/3)
    # let diff is 1 and c1 >c2
    elif n%3==1:
        c2=int((n-1)/3)
        c1=c2+1
    # diff is 1 but c2>c1
    else:
        c2=int((n+1)/3)
        c1=c2-1
    print(c1,end=" ")
    print(c2)
    t-=1


