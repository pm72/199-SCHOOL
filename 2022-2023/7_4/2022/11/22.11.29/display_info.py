from chess_players import players

w1 = 3
w2 = 20
w3 = 2 * w1 + 3 * w2 + len('Age')
ch = '-'


# HEADER
header = f"\n{' ':<{w1}s}" \
         f"{'Name':<{w2}s}" \
         f"{'Country':<{w2}s}" \
         f"{'Rating':<{w2}s}" \
         f"{'Age'}\n" \
         f"{ch * 69}"

# DSPLAY INFO
print(header)

for name, info in players.items():
  print(f"{' ':<{w1}s}" \
         f"{name:<{w2}s}" \
         f"{info.get('Country'):<{w2}s}" \
         f"{info.get('Rating'):<{w2}d}" \
         f"{info.get('Age')}\n" \
         f"{ch * 69}")
