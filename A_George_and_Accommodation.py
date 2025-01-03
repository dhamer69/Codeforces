n=int(input())
ct=0
for _ in range(n):
    n,m=map(int,input().split())
    if m-n>=2:
        ct+=1
print(ct)