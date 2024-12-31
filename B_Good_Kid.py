t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    product=1
    arr_min=min(arr)
    for i in range(n):
        if arr[i]==arr_min:
            arr[i]+=1
            break
    for i in range(n):
        product*=arr[i]
    print(product)
    t-=1