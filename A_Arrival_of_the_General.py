n = int(input()) 
arr = list(map(int, input().split())) 
max_index = arr.index(max(arr)) 
min_index =  arr[::-1].index(min(arr))  
moves = max_index + ( min_index)
if max_index > min_index:
        moves -= 1
print(moves)