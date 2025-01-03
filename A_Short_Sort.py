t=int(input())
while(t>0):
    s=input()
    if s[0]=="a":
        print("YES")
    else:
        if s[1]=="b":
            print("YES")
        elif s[0]=="b" and s[1]=="a":
            print("YES")
        else:
            print("NO")
    t-=1