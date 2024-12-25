t=int(input())
st=str(t)
ct=0
for i in range(len(st)):
    if st[i]=="4" or st[i]=="7":
        ct+=1
if ct==4 or ct==7:
    print("YES")
else:
    print("NO")
