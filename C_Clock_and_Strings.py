t=int(input())
while(t>0):
    a,b,c,d=map(int,input().split())
    # if c<max(a,b) and c>min(a,b):
    #     if d>max(a,b) or d<min(a,b):
    #         print("YES")
    #     else:
    #         print("NO")
    # elif d<max(a,b) and d>min(a,b):
    #     if c>max(a,b) or c<min(a,b):
    #         print("YES")
    #     else:
    #         print("NO")
    # else:
    #     print("NO")
    # t-=1

    # better soln
    s=""
    for i in range(1,13):
        if i==a or i==b:
            s+="a"
        if i==c or i==d:
            s+="b"
    print("YES" if s in ["abab","baba"] else "NO")
    t-=1