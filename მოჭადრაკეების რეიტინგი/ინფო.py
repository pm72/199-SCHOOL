from მოჭადრაკეები import players
from sys import exit

question = "0 – default\n" \
           "1 – Name\n" \
           "2 – Country\n" \
           "3 – Rating\n" \
           "4 – Age\n" \
           "Choose number for rating chess players: "

option = int(input(question))

if option == 0:
  option = "Default"
elif option == 1:
  option = "Name"
elif option == 2:
  option = "Country"
elif option == 3:
  option = "Rating"
elif option == 4:
  option = "Age"
else:
  print("\nInvalid choosing")
  print("Try again...\n")
  exit()

if option == 'Default':
  sorted_players = players.items()
elif option == "Name":
  sorted_players = sorted(players.items(), key=lambda i: i[0])
elif option == "Country":
  sorted_players = sorted(players.items(), key=lambda i: i[1].get(option))
else:
  sorted_players = sorted(players.items(),
                        key=lambda i: i[1].get(option),
                        reverse=True)

w1 = 3
w2 = 20
w3 = 2 * w1 + 3 * w2 + len('Age')
ch = '-'

# HEAD
head = f"\n{' ': <{w1}s}" \
       f"{'Name': <{w2}s}" \
       f"{'Country': <{w2}s}" \
       f"{'Rating': <{w2}s}" \
       f"{'Age'}\n" \
       f"{ch * w3}" \

# BODY
body = ''

for name, info in sorted_players:
  body += f"{' ': <{w1}s}" \
          f"{name: <{w2}s}" \
          f"{info.get('Country'): <{w2}s}" \
          f"{info.get('Rating'): <{w2}d}" \
          f"{info.get('Age')}\n" \
          f"{ch * w3}\n"

# DISPLAY PLAEYRS
print(head)
print(body)
