t=int(input())
while(t>0):
    s1,s2=map(str,input().rstrip().split())
    s11=""
    s22=""
    s11+=s2[0]
    s11+=s1[1]+s1[2]
    s22+=s1[0]
    s22+=s2[1]
    s22+=s2[2]
    print(s11 ,end=" ")
    print(s22)
    t-=1