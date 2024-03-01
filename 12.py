ATT = int(input("(ATT): "))
COMP = int(input("(COMP): "))
YDS = int(input("(YDS): "))
TD = int(input("(TD): "))
INT = int(input("(INT): "))

a = ((COMP / ATT) - 0.3) * 5
b = ((YDS / ATT) - 3) * 0.25
c = (TD / ATT) * 20
d = 2.375 - ((INT / ATT) * 25)
passer_rating = ((a + b + c + d) / 6) * 100

print(round(passer_rating, 2))
