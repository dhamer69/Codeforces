t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    s0=0
    s1=0
    ct1=0
    ct0=0
    for i in range(n):
        if i%2==0:
            s0+=a[i]
            ct0+=1
        else :
            s1+=a[i]
            ct1+=1
    if s0*ct1==s1*ct0 and (s0+s1)%n==0:
        print("YES")
    else:
        print("NO")
    t-=1