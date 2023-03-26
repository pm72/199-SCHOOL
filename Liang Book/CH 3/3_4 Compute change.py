# frecive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

remaining_amount = int(amount * 100)

number_of_laris = remaining_amount // 100

remaining_amount %= 100

number_of_50_tetris = remaining_amount // 50

remaining_amount %= 50

number_of_20_tetris = remaining_amount // 20

remaining_amount %= 20

number_of_10_tetris = remaining_amount // 10

remaining_amount %= 10

number_of_5_tetris = remaining_amount // 5

remaining_amount %= 5

number_of_2_tetris = remaining_amount // 2

remaining_amount %= 2

number_of_tetris = remaining_amount

print("Your amount", amount, "consists of\n",
      "\t", number_of_laris, "laris\n",
      "\t", number_of_50_tetris, "50 tetris\n",
      "\t", number_of_20_tetris, "20 tetris\n",
      "\t", number_of_10_tetris, "10 tetris\n"
      "\t", number_of_5_tetris, "5 tetris\n"
      "\t", number_of_2_tetris, "2 tetris\n"
      "\t", number_of_tetris, "tetris\n")
