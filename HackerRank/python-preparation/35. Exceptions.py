T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
