n,m=map(int,input().split())
l=[i for i in range(n+1,m+1)]
lst=[]
for i in l:
    for j in range(2,i):
        if i%j==0:
            lst.append(i)
            break 
newlst=[]
for i in l:
    if i in lst:
        pass
    else:
        newlst.append(i)

if m in lst :
    print("NO")
else:
    if len(newlst)>1:
        print("NO")
    else:
        print("YES")