from chess_players import players

w1 = 20
w2 = 3
ch = '–'
underline = 3*w1 + 2*w2 +3

# HEAD
print(f"{' ':<{w2}}"
      f"{'Player':<{w1}}"
      f"{'Country':<{w1}}"
      f"{'Rating':<{w1}}"
      f"{'Age'}")
print(ch * underline)

# BODY
for name, info in players.items():
      print(f"{' ':<{w2}}"
            f"{name:<{w1}}"
            f"{info.get('country'):<{w1}}"
            f"{info.get('rating'):<{w1}}"
            f"{info.get('age')}")
      print(ch * underline)