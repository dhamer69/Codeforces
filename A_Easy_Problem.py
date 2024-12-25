t=int(input())
while(t>0):
    l=[]
    n=int(input())
    for i in range(1,n):
        a=n-i
        l.append([a,i])
    print(len(l))
    t-=1