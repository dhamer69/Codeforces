t=int(input())
while(t>0):
    s=input()
    s1=""
    s2=""
    if (len(s))%2!=0:
        print("NO")
    else:
        for i in range(int(len(s)/2)):
            s1+=s[i]
        for j in range(int(len(s)/2),len(s)):
            s2+=s[j]
        if s1==s2:
            print("YES")
        else:
            print("NO")
    t-=1
        

