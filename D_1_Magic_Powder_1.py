n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def check(cnt,a,b,k):
    for i in range(n):
        need=a[i]*cnt
        if (b[i]>=need):
            continue
        k-=a[i]*cnt-b[i]
        if k<0:
            return False
    return True
low=0
high=1e9
while(low<=high):
    mid=int(low+(high-low)/2)
    if check(mid,a,b,k):
        low=mid+1
    else:
        high=mid-1
print(low-1)