from chess_players import players

w1 = 3
w2 = 20
w3 = 2 * w1 + 3 * w2 + len('Age')
ch = '-'

# HEAD
head = f"{' ':<{w1}s}" \
       f"{'Player':<{w2}s}" \
       f"{'Country':<{w2}s}" \
       f"{'Rating':<{w2}s}" \
       f"{'Age'}\n" \
       f"{ch * w3}"

# DISPLAY INFO
print(head)
