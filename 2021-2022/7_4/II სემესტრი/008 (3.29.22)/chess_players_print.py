from chess_players import players

w1 = 25
ch = '–'
amount_underline = w1 * 3 + 9
w2 = 3

# HEAD
print(f"{' ':<{w2}}"
      f"{'Player':<{w1}}"
      f"{'Country':<{w1}}"
      f"{'Rating':<{w1}}"
      f"{'Age'}")
print(ch * amount_underline)

for name, info in players.items():
  print(f"{' ':<{w2}}"
        f"{name:<{w1}}"
        f"{info.get('country'):<{w1}}"
        f"{info.get('rating'):<{w1}}"
        f"{info.get('age'):<{w1}}")
  print(ch * amount_underline)