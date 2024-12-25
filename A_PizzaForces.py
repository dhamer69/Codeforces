t=int(input())
while(t>0):
    n=int(input())
    '''sp -6 slice > 15 min
       mp -8 slice >>20 min
       lp--10 slice >> 25 min
       logic //
       let n=8 > n%6 =2 what we will do + 5+ 15 
       let say n=28%6=4 if reminder is 3,4 3 small +20
    '''
    ans=0
    rem=0
    if n<6:
        ans=15
        print(ans)
    else:
        rem=n%6
        if rem ==1 or rem==2:
            ans+=int((n//6))*15 + 5
        elif rem==0:
            ans+=int(n//6)*15
        elif rem==3 or rem==4:
            ans+=int((n//6))*15+10
        else:
            ans+=int(n//6+1)*15
        print(ans)
    t-=1