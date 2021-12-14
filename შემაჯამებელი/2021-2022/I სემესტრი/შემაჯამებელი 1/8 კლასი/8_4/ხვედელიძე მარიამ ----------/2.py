Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> kms = 14.0
miles = kms/1.6
minutes = 45.5
miles_in_1_minute = miles/minutes
miles_in_1_hour = miles_in_1_minute * 60
print(str(miles_in_1_hour) + " miles/hour")