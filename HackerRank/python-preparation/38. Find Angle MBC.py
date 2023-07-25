import math

AB = float(input())
BC = float(input())
AC = math.sqrt(AB ** 2 + BC ** 2)
CM = BM = AC / 2

cos_MBC = (BM ** 2 + BC ** 2 - CM ** 2) / (2 * BM * BC)
MBC_degrees = math.degrees(math.acos(cos_MBC))
degree_symbol = "\u00B0"
output = str(round(MBC_degrees)) + degree_symbol
print(output)
