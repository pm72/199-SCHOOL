amount = eval(input("Enter an amount, for example, 11.56: "))

remaining_amount = int(amount * 100)

amount_laris = remaining_amount // 100

remaining_amount %= 100

amount_50_tetris = remaining_amount // 50

remaining_amount %= 50

amount_20_tetris = remaining_amount // 20

remaining_amount %= 20

amount_10_tetris = remaining_amount // 10

remaining_amount %= 10

amount_5_tetris = remaining_amount // 5

remaining_amount = remaining_amount % 5   # remaining_amount %= 5

amount_2_tetris = remaining_amount // 2

remaining_amount %= 2

amount_of_tetris = remaining_amount

print("Your amount", amount, "consists of\n",
      "\t", amount_laris, "laris\n",
      "\t", amount_50_tetris, "50 tetris\n",
      "\t", amount_20_tetris, "20 tetris\n",
      "\t", amount_10_tetris, "10 tetris\n",
      "\t", amount_5_tetris, "5 tetris\n",
      "\t", amount_2_tetris, "2 tetris\n",
      "\t", amount_of_tetris, "tetris\n")
