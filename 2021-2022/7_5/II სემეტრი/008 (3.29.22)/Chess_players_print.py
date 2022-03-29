from chess_players import players

w1 = 25
w2 = 3
ch = '–'
underline = 84

print(players, "\n\n")

# HEAD
print(f"{' ':<{w2}}"
      f"{'Player':<{w1}}"
      f"{'Country':<{w1}}"
      f"{'Rating':<{w1}}"
      f"{'Age'}")
print(ch * underline)

for name, info in players.items():
  print(f"{' ':<{w2}}"
        f"{name:<{w1}}"
        f"{info.get('country'):<{w1}}"
        f"{info.get('rating'):<{w1}}"
        f"{info.get('age')}")
  print(ch * underline)