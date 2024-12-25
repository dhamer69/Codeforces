n=int(input())
a=list(map(int,input().split()))
a.sort()
sumi=0
for i in a:
    sumi+=i
ans=sumi/n
print(ans)