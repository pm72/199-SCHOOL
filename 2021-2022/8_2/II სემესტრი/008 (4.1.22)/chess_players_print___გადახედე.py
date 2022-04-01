from chess_players import players

w1 =25
w2 = 3
ch = '–'
underline = 3*w1 + 2*w2 + 3

 sorted(players.items(),
       key=lambda item: item[1].get('rating'),
       reverse=True)

# HEAD
print(f"{' ':<{w2}}"
      f"{'Player':<{w1}}"
      f"{'Country':<{w1}}"
      f"{'Rating':<{w1}}"
      f"{'Age'}")
print(ch * underline)

#BODY
for name, info in players.items():
  print(f"{' ':<{w2}}"
        f"{name:<{w1}}"
        f"{info.get('country'):<{w1}}"
        f"{info.get('rating'):<{w1}}"
        f"{info.get('age')}")
  print(ch * underline)