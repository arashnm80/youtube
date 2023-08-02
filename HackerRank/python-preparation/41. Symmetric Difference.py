input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))

symmetric_difference = a.union(b) - a.intersection(b)
symmetric_difference = sorted(symmetric_difference)
for x in symmetric_difference:
    print(x)
