for _ in range(int(input())):
    arr=list(map(int,input().split()))
    fib1=1
    fib2=1
    prev_sum=arr[0]+arr[1]
    if arr[1]+prev_sum==arr[2]:
        fib1+=1
    if arr[2]+prev_sum==arr[3]:
        fib1+=1

    prev_sum2=arr[2]-arr[1]
    if arr[2]+prev_sum2==arr[3]:
        fib2+=1
    print(max(fib1,fib2))
 

