from time import time

print(int(time()))

total_seconds = int(time())
seconds = total_seconds % 60

total_minutes = total_seconds // 60
minutes = total_minutes % 60

total_hours = total_minutes // 60
hours = total_hours % 24

print(f"Current time: {hours}:{minutes}:{seconds} GMT")
