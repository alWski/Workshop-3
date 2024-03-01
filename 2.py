num = int(input())
if 1 <= num <= 86400:
    hours = num // 3600  
    minutes = (num % 3600) // 60  
    seconds = (num % 3600) % 60  
print(hours, minutes, seconds)