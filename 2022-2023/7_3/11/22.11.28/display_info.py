from chess_players import players

header = f"{' ':<3s}" \
         f"{'Name':<20s}" \
         f"{'Country':<20s}" \
         f"{'Rating':<20s}" \
         f"{'Age'}\n" \
         f"{'-' * 69}"

body = ''
for name, info in players.items():
  body += f"{name}, info.get('Country'), info.get('Rating'), info.get('Age')"


print(header)
