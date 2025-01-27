for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=False
    for i in range(n):
        if arr[i]<=2*i or arr[i]<=(n-i-1)*2:
            ans=False
            break
        else:
            ans=True
    if ans :
        print("YES")
    else:
        print("NO")