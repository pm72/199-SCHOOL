##2)

lenght = 14
inputlenght = float(input("please input how much distance  you have passed in km:" ))
timeseconds = float(input("please input seconds: "))
timeminutes = float(input("please input minutes: "))
timehours = float(input("please input hours: "))

minutestohours = timeminutes/60
secondstohours = timeseconds/3600

totaltime = minutestohours + secondstohours + timehours

lenghtmph = inputlenght/1.6

milesperhour = lenghtmph/totaltime

print(milesperhour, "mph")