import re
import cmath

text = input()
text = text.replace(" ","")

pattern = r"([+-]?\d*)([+-]?\d*)j"
match = re.search(pattern, text)

x = int(match[1])
y = int(match[2])

number = complex(x, y)
r = abs(number)
fi = cmath.phase(number)

print(r)
print(fi)
