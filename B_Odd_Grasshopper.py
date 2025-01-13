t=int(input())
while(t>0):
    x,n=map(int,input().split())
    d=0
    if n%4==0:
        d=0
    elif n%4==1:
        d=-n
    elif n%4==2:
        d=1
    else:
        d=n+1
    if x%2==0:
        print(x+d)
    else:
        print(x-d)
    t-=1
