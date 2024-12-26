t=int(input())
while(t>0):
    n,m=map(int,input().split())
    words=[input() for _ in range(n)]
    total_len=0
    ct=0
    for word  in words:
        if total_len+len(word)<=m:
            total_len+=len(word)
            ct+=1
        else:
            break
    print(ct)
    t-=1
        