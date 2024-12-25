t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    hass=[0 for i in range(100)]
    for i in a:
        hass[i]+=1
    temp=0
    for i in range(len(hass)):
        if hass[i]==1:
            temp+=1

    ans =len(set(a))+temp%2
    print(ans)
    t-=1
