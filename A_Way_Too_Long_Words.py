n=int(input())
while(n>0):
    x=input()
    if len(x)>10:
        print(x[0]+str(len(x)-2)+x[-1])
    else:
        print(x)
    n-=1