t=int(input())
while(t>0):
    a,b,n=map(int,input().split())
    l=list(map(int,input().split()))
    max_time=b-1
    for i in range(n):
        # max_time+=(a-1) if (l[i] > a) else l[i]
        max_time+=min(l[i],a-1)
    

    print(max_time+1)
    t-=1