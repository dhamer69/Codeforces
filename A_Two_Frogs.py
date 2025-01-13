t=int(input())
while(t>0):
    n,a,b=map(int,input().split())
    if a%2==0 and b%2!=0 or a%2!=0 and b%2==0 :
        print("NO")
    else:
        print("YES")
    t-=1

