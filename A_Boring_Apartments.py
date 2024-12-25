t=int(input())
while(t>0):
    n=int(input())
    s=str(n)
    leni=len(s)
    ans=0
    ans=10*(int(s[0])-1)
    while(leni>0):
        ans+=leni
        leni-=1
    print(ans)
    t-=1


        
