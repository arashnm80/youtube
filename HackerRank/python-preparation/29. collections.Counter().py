from collections import Counter

X = int(input())
revenue = 0
myList = list(map(int, input().split()))
myCounter = Counter(myList)
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    if myCounter[x] > 0:
        myCounter[x] -= 1
        revenue += y
print(revenue)
    
        
