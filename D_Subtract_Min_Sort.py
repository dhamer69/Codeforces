# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     ans=False
#     i=0
#     while(i<n-1):
#         if arr[i]>arr[i+1]:
#             ans=True
#             break
#         else:
#             arr[i+1]-=arr[i]
#             arr[i]=0
#             i+=1
    
#     if ans:
#         print("NO")
#     else:
#         print("YES")
 
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n-1):
        a=l[i]
        b=l[i+1]
        z=min(a,b)
        l[i]=l[i]-z
        l[i+1]=l[i+1]-z
    l1=l.copy()
    l.sort()
    if l1==l:
        print("YES")
    else:
        print("NO")
