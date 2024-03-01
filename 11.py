import math

a, b, c = map(float, input().split())

A = round(math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * 180 / 3.14, 2)
B = round(math.acos((a**2 + c**2 - b**2) / (2 * a * c)) * 180 / 3.14, 2)
C = round(180 - A - B, 2)

print(A, B, C)
