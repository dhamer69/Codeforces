for _ in range(int(input())):
    l,r=map(int,input().split())
    if l==1 and r==1 :
        ans =1
    else:
        ans=r-l
    print(ans)
