x=input()
y=""
if x[0].isupper():
    print(x)
else:
    y=x[0].capitalize()
    for i in range(1,len(x)):
        y+=x[i]
    print(y)
    





