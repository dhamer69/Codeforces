n=int(input())
# a=no of ppl exist 
# b=no of ppl ent
max_cap=0
curren_cap=0
for _ in range(n):
    lst=list(map(int,input().rstrip().split()))
    a=lst[0]
    b=lst[1]
    curren_cap+=b-a
    if curren_cap>max_cap:
        max_cap=curren_cap
print(max_cap)