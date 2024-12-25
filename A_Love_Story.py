t=int(input())
while(t>0):
    s=input()
    ct=0
    love="codeforces"
    for i in range(len(s)):
        for j in range(len(love)):
            if i==j:
                if s[i]!=love[j]:
                    ct+=1
    print(ct)
    t-=1