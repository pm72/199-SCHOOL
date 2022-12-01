from chess_players import players
import csv, os

sorted_players = sorted(players.items(),
                        key=lambda i: i[1].get('Rating'),
                        reverse=True)

COLUMNS = ['Name', 'Country', 'Rating', 'Age']
FILENAME = "sorted_players.csv"

with open(FILENAME, 'w', newline='') as file:
  w = csv.DictWriter(file, fieldnames=COLUMNS)
  w.writeheader()

  row = {}
  for name, info in sorted_players:
    row[COLUMNS[0]] = name
    row[COLUMNS[1]] = info.get('Country')
    row[COLUMNS[2]] = info.get('Rating')
    row[COLUMNS[3]] = info.get('Age')

    w.writerow(row)

os.startfile(FILENAME)
  


##print(sorted_players[0])
##print(sorted_players[0][0], end=' ')
##print(sorted_players[0][1].get('Country'), end=' ')
##print(sorted_players[0][1].get('Rating'), end=' ')
##print(sorted_players[0][1].get('Age'), end=' ')
