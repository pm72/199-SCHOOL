w1 = 3
w2 = 20
w3 = 2 * w1 + 3* w2 + len('Age')
ch = '-'

# HEAD
head = f"{' ':<3s}"\
       f"{'Player':<20s}" \
       f"{'Country':<20s}" \
       f"{'Rating':<20s}" \
       f"{'Age'}\n" \
       f"{'-' * 69}"

# INFO
info = f"{' ':<3s}"\
       f"{'Jobava':<20s}" \
       f"{'Georgia':<20s}" \
       f"{2588:<20d}" \
       f"{38}\n" \
       f"{'-' * 69}\n"

info += f"{' ':<3s}"\
        f"{'Caruana':<20s}" \
        f"{'USA':<20s}" \
        f"{2781:<20d}" \
        f"{29}\n" \
        f"{'-' * 69}\n"

# DISPLAY INFO
print(head)
print(info)
