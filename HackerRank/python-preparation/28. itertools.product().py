from itertools import product

A = map(int, input().split())
B = map(int, input().split())

AxB = product(A, B)

for i in AxB:
    print(i, end=" ")
