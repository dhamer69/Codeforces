
t=int(input())
while(t>0):
    a,b=map(int,input().split())
    max_gcd=abs(a-b)
    if a==b:
        moves=0
    elif a>b:
        moves=min(b%max_gcd,max_gcd-b%max_gcd)
    else :
        moves=min(a%max_gcd,max_gcd-a%max_gcd)

    print(max_gcd,end=" ")
    print(moves)
    t-=1

