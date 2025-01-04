from collections import Counter

t = int(input())
while t > 0:
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # Count frequencies
    freq = Counter(arr)
    freq_list = sorted(freq.values())  # Sort frequencies in ascending order

    # Calculate the number of distinct groups after replacements
    for i in range(len(freq_list)):
        if k >= freq_list[i]:
            k -= freq_list[i]
        else:
            break
    ans = len(freq_list) - i  # Remaining groups after using k replacements
    print(ans)

    t -= 1