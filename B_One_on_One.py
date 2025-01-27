for _ in range(int(input())):
    n,m=map(int,input().split())
    cnt=0
    prev_arr=list(map(int,input().split()))
    for _ in range(n-1):
        arr=list(map(int,input().split()))
        for i in range(m-1):
            if prev_arr[i]==arr[i]==1 and arr[i+1]==prev_arr[i+1]==1:
                cnt+=1
        prev_arr=arr
    print(cnt)

