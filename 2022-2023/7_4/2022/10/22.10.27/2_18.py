from time import time

gmt = int(input("Enter your time zone [-12 .. 12]: "))

print(int(time()))

total_seconds = int(time())
seconds = total_seconds % 60

total_minutes = total_seconds // 60
minutes = total_minutes % 60

total_hours = total_minutes // 60
hours = total_hours % 24

print(f"Current time: {(hours + gmt) % 24}:{minutes}:{seconds} GMT{gmt}")
