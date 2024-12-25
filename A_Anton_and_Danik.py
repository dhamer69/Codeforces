n=int(input())
st=input()
ct1=0
ct2=0
for i in range(n):
    if st[i]=="A":
        ct1+=1
    else:
        ct2+=1
if ct1>ct2:
    print("Anton")
elif ct1==ct2:
    print("Friendship")
else:
    print("Danik")