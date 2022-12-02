from chess_players import players
import csv, os

sorted_players = sorted(players.items(),
                        key=lambda i: i[1].get('Rating'),
                        reverse=True)

FILENAME = "chess players sorted by rating.csv"
COLUMNS = ('Name', 'Country', 'Rating', 'Age')

with open(FILENAME, mode='w', newline='') as file:
  w = csv.DictWriter(file, fieldnames=COLUMNS)

  w.writeheader()

  for name, info in sorted_players:
   player = {
     'Name': name,
     'Country': info.get('Country'),
     'Rating': info.get('Rating'),
     'Age': info.get('Age'),
     }

   w.writerow(player)

os.startfile(FILENAME)
