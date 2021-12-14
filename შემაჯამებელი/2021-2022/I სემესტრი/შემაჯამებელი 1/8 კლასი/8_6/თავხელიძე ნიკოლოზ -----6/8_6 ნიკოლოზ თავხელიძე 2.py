distance=14
time_in_minutes=45
time_in_seconds=30
distance/=1.6
time_in_hours=(time_in_minutes*60+time_in_seconds)//3600
print(distance//time_in_hours, 'miles per hour')