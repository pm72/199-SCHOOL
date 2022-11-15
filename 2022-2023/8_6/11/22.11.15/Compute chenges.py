##11.56
##
##int(11.56 * 100)          1156
##
##1156 // 100               11 gel
##1156 % 100                56 tetri
##
##56 // 50                  1 50 tetri
##56 % 50                   6 teti
##
##6 // 20                   0 20 tetri
##6 % 20                    6 tetri
##
##6 // 10                   0 10 tetri
##6 % 10                    6 tetri
##
##6 // 5                    1 5 tetri
##6 % 5                     1 tetri
##
##1 // 2                    0 2 tetri
##1 % 2                     1 tetri
##
##1                         1 1 tetri

amount = eval(input("Enter an amount, for example, 11.56: "))

remaining_amount = int(amount * 100)

amount_of_laris = remaining_amount // 100

remaining_amount = remaining_amount % 100

amount_of_50_tetris = remaining_amount // 50

remaining_amount %= 50

amount_of_20_tetris = remaining_amount // 20

remaining_amount %= 20

amount_of_10_tetris = remaining_amount // 10

remaining_amount %= 10

amount_of_5_tetris = remaining_amount // 5

remaining_amount %= 5

amount_of_2_tetris = remaining_amount // 2

remaining_amount %= 2

print("Your amount", amount, "consists of\n",
      "\t",amount_of_laris, "laris\n",
      "\t", amount_of_50_tetris, "50 tetris\n",
      "\t", amount_of_20_tetris, "20 tetris\n",
      "\t", amount_of_10_tetris, "10 tetris\n",
      "\t", amount_of_5_tetris, "5 tetris\n",
      "\t", amount_of_2_tetris, "2 tetris\n"
      "\t", remaining_amount, "tetris\n")
