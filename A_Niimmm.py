# arr=[10, 20, 30, 40, 50]
# l=[]
# for i in range(len(arr)):
#     if arr[i+1]>arr[i]:
#         l.append(arr[i])
# if l==arr:
#     print(True)
# else:
#     print(False)
st="aooo"
l=list(st)
l=list(dict.fromkeys(l))
print(l)
output="".join(l)
print(output)