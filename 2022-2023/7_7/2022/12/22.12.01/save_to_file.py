from chess_players import players
import csv, os

sorted_players = sorted(players.items(),
                        key=lambda a: a[1].get('Rating'),
                        reverse=True)

FILENAME = "sorted_players.csv"
COLUMNS = ["Name", "Country", "Rating", "Age"]

with open(FILENAME, 'w', newline='') as file:
  w = csv.DictWriter(file, fieldnames=COLUMNS)

  w.writeheader()

  for name, info in sorted_players:
    row = {'Name': name}
    row['Country'] = info.get('Country')
    row['Rating'] = info.get('Rating')
    row['Age'] = info.get('Age')

    w.writerow(row)

os.startfile(FILENAME)
