t=int(input())
while(t>0):
    n,m,q=map(int,input().split())
    b1,b2=map(int,input().split())
    a1=int(input())
    if a1==1 or a1==n:
        ans=min(abs(a1-b1),abs(a1-b2))
    else:
        if b1>a1 and b2>a1:
            ans=min(b1-1,b2-1)
        elif a1>b1 and a1>b2:
            ans=min(n-b1,n-b2)
        else:
            ans=min(abs(int((b1+b2)/2)-b1),abs(int((b1+b2)/2)-b2))
    print(ans)
    t-=1
