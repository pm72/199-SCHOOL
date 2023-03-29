def tax(income):
  fix10 = 11950
  fix15 = 45500
  fix25 = 117450
  fix28 = 190200
  fix33 = 372950

  if income <= fix10:
    tax = income * 0.1
  elif income <= fix15:
    tax = fix10 * 0.1 + (income - fix10) * 0.15
  elif income <= fix25:
    tax = fix10 * 0.1 + (fix15 - fix10) * 0.15 + \
          (income - fix15) * 0.25
  elif income <= fix28:
    tax = fix10 * 0.1 + (fix15 - fix10) * 0.15 + \
          (fix25 - fix15) * 0.25 + (income - fix25) * 0.28
  elif income <= fix33:
    tax = fix10 * 0.1 + (fix15 - fix10) * 0.15 + \
          (fix25 - fix15) * 0.25 + (fix28 - fix25) * 0.28 + \
          (income - fix28) * 0.33
  else:
    tax = fix10 * 0.1 + (fix15 - fix10) * 0.15 + \
          (fix25 - fix15) * 0.25 + (fix28 - fix25) * 0.28 + \
          (fix33 - fix28) * 0.33 + (income - fix33) * 0.35

  return tax
