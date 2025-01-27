for _ in range(int(input())):
    a,c=map(int,input().split())
    if a==0:
        ans =c
    else:
        ans=c%a
    print(ans)