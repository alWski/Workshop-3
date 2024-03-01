X, Y, N = map(int, input().split())

i = (X * 100 + Y) * N
rub = i // 100
kop = i % 100

print(f"{rub} руб. {kop} коп.")
