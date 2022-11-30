from chess_players import players

w1 = 3
w2 = 20
w3 = 2 * w1 + 3 * w2 + len('Age')
ch = '-'

a = list(players.items())
print(a[0])
print(a[0][1])
print(a[0][1].get('Country'))

##sorted_player = sorted(players.items(),
##                       key = lambda i: i[0])
##
### HEADER
##header = f"\n{' ':<{w1}s}" \
##         f"{'Name':<{w2}s}" \
##         f"{'Country':<{w2}s}" \
##         f"{'Rating':<{w2}s}" \
##         f"{'Age'}\n" \
##         f"{ch * w3}"
##
### DISPLAY INFO
##print(header)
##
##for name, info in sorted_player :
##  print(f"{' ':<{w1}s}" \
##         f"{name:<{w2}s}" \
##         f"{info.get('Country'):<{w2}s}" \
##         f"{info.get('Rating'):<{w2}d}" \
##         f"{info.get('Age')}\n" \
##         f"{ch * w3}")
