t=int(input())
while(t>0):
    n=int(input())
    x=1
    cnt=1
    last_sum=1
    while(x<n):
        x=2*(1+last_sum)
        last_sum=x
        cnt+=1
    print(cnt)
    t-=1
    