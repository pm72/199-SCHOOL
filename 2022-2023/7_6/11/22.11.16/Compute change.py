amount = eval(input("Enter an amount: "))

remaining_amount = int(amount * 100)

amount_of_laris = remaining_amount // 100
remaining_amount = remaining_amount % 100

amount_of_50_tetris = remaining_amount // 50
remaining_amount = remaining_amount % 50

amount_of_20_tetris = remaining_amount // 20
remaining_amount = remaining_amount % 20

amount_of_10_tetris = remaining_amount // 10
remaining_amount = remaining_amount % 10

amount_of_5_tetris = remaining_amount // 5
remaining_amount = remaining_amount % 5

amount_of_2_tetris = remaining_amount // 2
remaining_amount = remaining_amount % 2


print("Your amount", amount, "consists of\n",
      "\t", amount_of_laris, "laris\n",
      "\t", amount_of_50_tetris, "50 tetris\n",
      "\t", amount_of_20_tetris,  "20 tetris\n",
      "\t", amount_of_10_tetris, "10 tetris\n",
      "\t", amount_of_5_tetris, "5 tetris\n",
      "\t", amount_of_2_tetris, "2 tetris\n",
      "\t", remaining_amount, "1 tetri\n",)
