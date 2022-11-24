w1 = 3
w2 = 20
w3 = 2 * w1 + 3 * w2 + len('Age')

print(f"{'-' * w3}"
      f"{' ':<{w1}s}"
      f"{'Player':<{w2}s}"
      f"{'Country':<{w2}s}"
      f"{'Rating':<{w2}s}"
      f"{'Age'}\n"
      f"{'-' * w3}")

print(f"{' ':<{w1}s}"
      f"{'Jobava':<{w2}s}"
      f"{'Georgia':<{w2}s}"
      f"{2588:<{w2}d}"
      f"{38}\n"
      f"{'-' * w3}")

print(f"{' ':<{w1}s}"
      f"{'Caruana':<{w2}s}"
      f"{'USA':<{w2}s}"
      f"{2781:<{w2}d}"
      f"{29}\n"
      f"{'-' * w3}")
