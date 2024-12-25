s1=input()
s2=input()
ans=""
for i in range(len(s1)):
        for j in range(len(s2)):
                if i==j:
                    ans+=str(int(s1[i])^int(s2[j]))
print(ans)