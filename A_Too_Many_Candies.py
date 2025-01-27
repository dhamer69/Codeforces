for _ in range(int(input())):
    n,m=map(int,input().split())
    if n<m or m==0:
        print("0",end=" ")
        print(n)
    else:
            candies=n%m
            print(n-candies,end=" ")
            print(candies)