total_sec = int(input("Enter amount seconds: "))

hour = total_sec // 3600
minute = total_sec % 3600 // 60
sec = total_sec % 60

print(hour, minute, sec, sep=':')
