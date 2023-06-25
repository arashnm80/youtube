N, M = map(int, input().split())

for i in range(int((N - 1) / 2)):
    pack = ".|."
    text = ((i * 2) + 1) * pack
    print(text.center(M,"-"))

print("WELCOME".center(M, "-"))
    
for i in reversed(range(int((N - 1) / 2))):
    pack = ".|."
    text = ((i * 2) + 1) * pack
    print(text.center(M,"-"))
