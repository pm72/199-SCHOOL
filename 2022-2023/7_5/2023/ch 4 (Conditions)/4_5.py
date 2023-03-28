'''
0 - კვირა
1 - ორშაბათი
2 - სამშაბათი
3 - ოთხშაბათი
4 - ხუთშაბათი
5 - პარასკევი
6 - შაბათი

'''

s = "0 - კვირა\n" + \
    "1 - ორშაბათი\n" + \
    "2 - სამშაბათი\n" + \
    "3 - ოთხშაბათი\n" + \
    "4 - ხუთშაბათი\n" + \
    "5 - პარასკევი\n" + \
    "6 - შაბათი\n"


print(s)
today = -1

while today < 0 or today > 6:
  today = int(input("შეიტანეთ დღე ციფრის სახით: "))

offset = int(input("მიმდინარე დღიდან გასული დღეების რაოდენობა: "))

days = (today + offset) % 7

if today == 0: today = "კვირა"
elif today == 1:  today = "ორშაბათი"
elif today == 2: today = "სამშაბათი"
elif today == 3: today = "ოთხშაბათი"
elif today == 4: today = "ხუთშაბათი"
elif today == 5: today = "პარასკევი"
else: today = "შაბათი"

if days == 0: s = f"მიმდინარე დღეა {today}, " + \
                  "{offset} დღის შემდეგ იქნება {days}"

print(s)
  
