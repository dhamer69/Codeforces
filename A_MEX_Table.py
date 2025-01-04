t=int(input())
while(t>0):
    n,m=map(int,input().split())
    ans=0
    ans+=max(n,m)+1
    print(ans)
    t-=1