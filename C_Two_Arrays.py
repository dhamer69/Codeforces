t=int(input())
while(t>0):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr1.sort()
    arr2.sort()
    for i in range(n):
        if arr2[i]-arr1[i]==1 or arr2[i]-arr1[i]==0:
            ans=True
        else:
            ans=False
            break
    if ans :
        print("YES")
    else:
        print("NO")
    t-=1