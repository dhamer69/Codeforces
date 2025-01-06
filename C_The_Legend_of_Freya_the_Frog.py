t=int(input())
while(t>0):
    x,y,k=map(int,input().split())
    x=int((x+k-1)/k)
    y=int((y+k-1)/k)
    print(max((2*x-1),2*y))
    t-=1