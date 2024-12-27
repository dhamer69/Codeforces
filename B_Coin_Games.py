t=int(input())
while(t>0):
    n=int(input())
    s=input()
    '''
    concept is simple firstly obs  if there is odd num of "U" then alice 
    will win for sure and if even then alice will loose and we perform
    any of operation u will observe that if there were odd "U" before it will still 
    remain odd no of "U" after performing the oper..

    '''

    sumi=0
    for i in range(n):
        if s[i]=="U":
            sumi+=1
    # print(sumi)
    if sumi%2!=0:
        print("YES")
    else:
        print("NO")
    t-=1