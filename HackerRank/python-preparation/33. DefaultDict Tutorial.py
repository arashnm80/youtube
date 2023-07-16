from collections import defaultdict
n, m = map(int, input().split())

d = defaultdict(list)

for i in range(n):
    x = input()
    d[x].append(i + 1)
    
for i in range(m):
    x = input()
    if bool(d[x]):
        print(" ".join(map(str,d[x])))
    else:
        print(-1)
