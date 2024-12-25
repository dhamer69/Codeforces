t=int(input())
while(t>0):
    ans=""
    s=input()
    for i in s:
        if i=="p":
            ans+="q"
        elif i=="q":
            ans+="p"
        else:
            ans+="w"
    print(ans[::-1])
    t-=1
            