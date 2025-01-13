t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=True
    dup_arr=arr.copy()
    arr.sort()
    for i in range(n):
        if abs(arr[i]-dup_arr[i])>1:
            ans=False
            break
        else:
            ans=True
    if ans:
        print("YES")
    else:
        print("NO")
    t-=1