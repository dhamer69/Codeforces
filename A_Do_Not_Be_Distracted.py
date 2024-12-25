# t=int(input())
# while(t>0):
#     n=int(input())
#     s=input()
#     s.lower()
#     j=0
#     a=[0 for i in range(27)]
#     for i in range(n):
#         a[ord(s[i])-ord("a")]+=1
#         if a[ord(s[i])-ord("a")]>1 and s[i-1]!=s[i]:
#             j=1
#             break
#     if j:
#         print("NO")
#     else:
#         print("YES")
#     t-=1