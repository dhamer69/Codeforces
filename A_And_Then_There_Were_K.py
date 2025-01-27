for _ in range(int(input())):
    n=int(input())
    x=1
    while(True):
        if x*2>n:
            print(x-1)
            break
        else:
            x*=2
        