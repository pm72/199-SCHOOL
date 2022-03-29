from chess_players import players

w1 = 25
ch = '–'
amount_ch = w1 * 3 + 9
w2 = 3

# HEAD
print(f"{' ':<{w2}}"
      f"{'Player':<{w1}}"
      f"{'Country':<{w1}}"
      f"{'Rating':<{w1}}"
      f"{'Age':<{w1}}")
print(ch * amount_ch)

# BODY
for name, info in players.items():
  print(f"{' ':<{w2}}"
        f"{name:<{w1}}"
        f"{info.get('country'):<{w1}}"
        f"{info.get('rating'):<{w1}}"
        f"{info.get('age')}")
  print(ch * amount_ch)