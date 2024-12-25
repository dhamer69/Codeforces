n=int(input())
layer=[]
for i in range(1,n+1):
   if i%2==0:
      layer.append("I love")
   else:
      layer.append("I hate")

ans=" that "  .join(layer)+ " it"
print(ans)