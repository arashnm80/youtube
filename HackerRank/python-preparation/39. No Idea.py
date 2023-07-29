# run in pypy 3
n, m = map(int, input().split())
my_list = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

happiness = 0

for x in my_list:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1
        
print(happiness)
