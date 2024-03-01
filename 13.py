X, Y = map(int, input().split())
result = ((X % Y) * (Y % X)) + 1
print(result)