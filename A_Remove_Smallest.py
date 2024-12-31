t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    i,j=0,1
    while(i<n and j<n):
        if j<n and i<n: 
            if abs(arr[i]-arr[j])<=1:
                arr.remove(min(arr[i],arr[j]))
                i+=1
                j+=1
        else:
            break
    if len(arr)>1:
        print("NO") 
    else:
        print("YES")
    t-=1


