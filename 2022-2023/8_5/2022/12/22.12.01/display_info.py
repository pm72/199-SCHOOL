from chess_players import players

# SPACES
w1 = 3
w2 = 20
w3 = 2 * w1 + 3 * w2 + len('Age')
ch = '-'

sorted_players = sorted(players.items())

sorted_players = sorted(players.items(),
                        key=lambda i: i[1].get('Country'),
                        reverse=False)

# HEAD
head = f"\n{' ':<{w1}s}" \
       f"{'Name':<{w2}s}" \
       f"{'Country':<{w2}s}" \
       f"{'Rating':<{w2}s}" \
       f"{'Age'}\n" \
       f"{ch * w3}"

# DISPLAY INFO
print(head)

for name, info in sorted_players:
  print(f"{' ':<{w1}s}" \
       f"{name:<{w2}s}" \
       f"{info.get('Country'):<{w2}s}" \
       f"{info.get('Rating'):<{w2}d}" \
       f"{info.get('Age')}\n" \
       f"{ch * w3}")
