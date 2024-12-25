t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if a[i]==0 and a[i-1]>0 :
            ans+=1
    print(min(ans,2))
    t-=1