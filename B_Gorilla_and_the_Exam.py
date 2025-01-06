from collections import Counter

t = int(input())
while t > 0:
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    freq_list = sorted(freq.values())  

   
    for i in range(len(freq_list)):
        if k >= freq_list[i]:
            k -= freq_list[i]
        else:
            break
    ans = len(freq_list) - i 
    print(ans)

    t -= 1