n,m=map(int,input().split())
ct=0
while(n<=m):
    ct+=1
    n*=3
    m*=2
print(ct)