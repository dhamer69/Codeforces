for _ in range(int(input())):
    n,m=map(int,input().split())
    total=n*4*m
    for i in range(n):
        x,y=map(int,input().split())
        if i==0:
            continue
        else:

            total-=2*(m-x+m-y)
    print(total)