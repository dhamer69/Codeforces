t=int(input())
while(t>0):
    x,y,n=map(int,input().split())

    '''
    what is thought process first find out n%x for eg :
    n=4  and x=5 and y=0
    4%5=4 now we have to reduce some value from so that it rem become y in this case 0
    ok now n-1=3%5=3...2..1..0 /we kept dec n
    now we have to check how many steps we need to do in this that will be 
    (rem-y+x)%x 
    in this case 
    rem=4 and y=0 and x=5
    (4-0+5)%5=4 why we used so that we can escape that neg case /// i.e(rem-y )<0
    '''
    rem=n%x
    change=(rem-y+x)%x
    print(n-change)
    t-=1