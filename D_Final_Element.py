t=int(input())
while(t>0):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    persent=False
    if n==1:
        if arr[0]==k:
            persent=True
    i=0
    j=1
    while(i<n and j<n):
        if abs(arr[i]-arr[j])==k:
            persent=True
            break
        elif (arr[i]+abs(k)<arr[j]):
            i+=1
        else:
            j+=1
    if persent:
        print("YES")
    else:
        print("NO")
    t-=1