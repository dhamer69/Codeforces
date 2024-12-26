t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    s0=0
    s1=0
    ct1=0
    ct0=0
    # s0 sum of even place 
    # s1 sum of odd places.
    # ct1 no of odd place/index
    # ct0 no of even places
    for i in range(n):
        if i%2==0:
            s0+=a[i]
            ct0+=1
        else :
            s1+=a[i]
            ct1+=1

    # dis is of num in odd and even place condns
    if s0*ct1==s1*ct0 and (s0+s1)%n==0:
        print("YES")
    else:
        print("NO")
    t-=1
